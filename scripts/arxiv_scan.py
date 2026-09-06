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
QUERIES = [
    ('loco-manipulation', 'all:"humanoid" AND all:"loco-manipulation"'),
    ('whole-body-control', 'all:"humanoid" AND all:"whole-body control"'),
    ('mobile-manipulation', 'all:"humanoid" AND all:"mobile manipulation"'),
    ('whole-body-manipulation', 'all:"humanoid" AND all:"whole-body manipulation"'),
    ('teleoperation', 'all:"humanoid" AND all:"teleoperation"'),
    ('vla-humanoid', 'all:"humanoid" AND all:"vision-language-action"'),
    ('bimanual', 'all:"humanoid" AND all:"bimanual"'),
    ('motion-retargeting', 'all:"humanoid" AND all:"motion retargeting"'),
    ('locomotion-manipulation', 'all:"humanoid" AND all:"locomotion" AND all:"manipulation"'),
]


def fetch(url):
    return urllib.request.urlopen(url, timeout=30).read()


def existing_ids():
    try:
        text = fetch(REPO_PAPERS).decode("utf-8")
        return set(re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", text))
    except Exception:
        return set()


def main():
    # cutoff date
    if os.path.exists(MARKER):
        cutoff = open(MARKER).read().strip()
    else:
        import datetime
        cutoff = (datetime.date.today() - datetime.timedelta(days=LOOKBACK_DAYS)).isoformat()

    known = existing_ids()
    seen = {}
    for tag, q in QUERIES:
        url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"search_query": q, "start": 0, "max_results": 25,
             "sortBy": "submittedDate", "sortOrder": "descending"})
        try:
            root = ET.fromstring(fetch(url))
        except Exception as e:
            print(f"<!-- query {tag} failed: {e} -->", file=sys.stderr)
            time.sleep(3)
            continue
        for e in root.findall("a:entry", NS):
            aid = e.find("a:id", NS).text.split("/abs/")[-1]
            pub = e.find("a:published", NS).text[:10]
            title = " ".join(e.find("a:title", NS).text.split())
            authors = [a.find("a:name", NS).text for a in e.findall("a:author", NS)]
            au = authors[0] + (" et al." if len(authors) > 1 else "")
            if pub > cutoff and aid not in known and aid not in seen:
                seen[aid] = (pub, title, au)
        time.sleep(3)

    # update marker to the newest paper found (or today)
    newest = max([v[0] for v in seen.values()] + [cutoff])
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
