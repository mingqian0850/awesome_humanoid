#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Weekly arXiv sweep for humanoid loco-manipulation papers.

Queries arXiv (9 keyword groups), keeps papers newer than the marker date,
and prints a ready-to-paste issue body (or nothing when no new papers).
Run from the repo root. Requires no external packages (urllib only).
"""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import os
import sys
import re

MARKER = os.path.join(os.path.dirname(__file__), ".last_scan")
REPO_PAPERS = "https://raw.githubusercontent.com/mingqian0850/awesome_humanoid/main/papers.md"
LOOKBACK_DAYS = 14

NS = {"a": "http://www.w3.org/2005/Atom"}
# 合并为 3 组 OR 查询（而不是 9 组），把每次运行的请求数从 9 降到 3，
# 显著降低被 arXiv 限流（HTTP 429）的概率。
QUERIES = [
    ('loco-manip',
     'all:"humanoid" AND (all:"loco-manipulation" OR all:"whole-body control" '
     'OR all:"whole-body manipulation" OR all:"mobile manipulation")'),
    ('teleop-data',
     'all:"humanoid" AND (all:"teleoperation" OR all:"motion retargeting" '
     'OR all:"bimanual" OR all:"vision-language-action")'),
    ('broad-catch',
     'all:"humanoid" AND all:"locomotion" AND all:"manipulation"'),
]
MAX_RESULTS = 100


def fetch(url, attempts=2, backoff=8):
    """GET with retry/backoff (arXiv API returns 429 when polled too fast)."""
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "awesome-humanoid-scan/1.0"})
            return urllib.request.urlopen(req, timeout=30).read()
        except Exception as e:
            last = e
            if i < attempts - 1:
                time.sleep(backoff * (i + 1))
    raise last


def existing_ids():
    try:
        text = fetch(REPO_PAPERS).decode("utf-8")
        return set(re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", text))
    except Exception:
        return set()


def dismissed_ids():
    """IDs intentionally skipped by the maintainer (kept out of future scans)."""
    path = os.path.join(os.path.dirname(__file__), "dismissed.txt")
    if not os.path.exists(path):
        return set()
    ids = set()
    for line in open(path, encoding="utf-8"):
        line = line.split("#")[0].strip()
        if line:
            ids.add(line.split()[0])
    return ids


def main():
    import datetime
    # cutoff date
    if os.path.exists(MARKER):
        cutoff = open(MARKER).read().strip()
    else:
        cutoff = (datetime.date.today() - datetime.timedelta(days=LOOKBACK_DAYS)).isoformat()

    known = existing_ids()
    skip = dismissed_ids()
    seen = {}
    scanned = []
    ok_queries = 0
    for tag, q in QUERIES:
        url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"search_query": q, "start": 0, "max_results": MAX_RESULTS,
             "sortBy": "submittedDate", "sortOrder": "descending"})
        try:
            root = ET.fromstring(fetch(url))
            ok_queries += 1
        except Exception as e:
            print(f"<!-- query {tag} failed: {e} -->", file=sys.stderr)
            time.sleep(3)
            continue
        for e in root.findall("a:entry", NS):
            # 去掉版本后缀（v1/v2…），与 papers.md / dismissed.txt 中的无版本 ID 对齐
            aid = re.sub(r"v\d+$", "", e.find("a:id", NS).text.split("/abs/")[-1])
            pub = e.find("a:published", NS).text[:10]
            title = " ".join(e.find("a:title", NS).text.split())
            authors = [a.find("a:name", NS).text for a in e.findall("a:author", NS)]
            au = authors[0] + (" et al." if len(authors) > 1 else "")
            scanned.append(pub)
            if pub > cutoff and aid not in known and aid not in skip and aid not in seen:
                seen[aid] = (pub, title, au)
        time.sleep(3)

    # 只有全部关键词组都成功时才推进 marker：部分/全部查询失败时保持不变，
    # 以免漏掉论文（下次运行会重新扫描）。
    if ok_queries < len(QUERIES):
        print(f"仅 {ok_queries}/{len(QUERIES)} 组查询成功，marker 保持不变（{cutoff}），本次不产出候选",
              file=sys.stderr)
        print("")
        sys.exit(0)

    # 全部成功时把 marker 推进到扫到的最新日期（或今天），
    # 这样人工判定「不收录」的条目不会每周重复出现（也在 dismissed.txt 中登记）。
    newest = max(scanned + [cutoff, datetime.date.today().isoformat()])
    with open(MARKER, "w") as f:
        f.write(newest)

    if not seen:
        print("")
        return
    lines = [
        "## 🤖 本周 arXiv 新论文候选（自动扫描，需人工筛选）",
        "",
        f"> 扫描时间：{newest} 之后提交 · 关键词组：{len(QUERIES)} 组 · 自动与 papers.md 已有条目去重。"
        "以下为**候选**，人工确认相关性与链接后手动加入 papers.md（自动流程不做语义筛选）。",
        "",
    ]
    for aid in sorted(seen, key=lambda k: seen[k][0], reverse=True):
        pub, title, au = seen[aid]
        lines.append(f"- **{title}** — {au}, arXiv {pub}. [arXiv](https://arxiv.org/abs/{aid})")
    lines.append("")
    lines.append("<!-- 由 .github/workflows/arxiv-weekly.yml 自动创建 -->")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
