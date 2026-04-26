#!/usr/bin/env python3
"""Generate index.md from the submissions/ folder.

Fetches problem titles and difficulty from the LeetCode GraphQL API when
credentials are available. Pass via env vars LEETCODE_SESSION and
LEETCODE_CSRF_TOKEN, or as CLI args --session / --csrf-token.
Falls back to slug-derived titles and blank difficulty if unavailable.
"""
import argparse
import json
import os
import re
import urllib.request

SUBMISSIONS_DIR = "submissions"
OUTPUT_FILE = "index.md"
LEETCODE_BASE = "https://leetcode.com/problems"
GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query {
  problemsetQuestionList: questionList(
    categorySlug: ""
    limit: 3000
    skip: 0
    filters: {}
  ) {
    questions: data {
      titleSlug
      title
      difficulty
    }
  }
}
"""


def fetch_problem_data(session: str, csrf_token: str) -> dict:
    payload = json.dumps({"query": QUERY}).encode()
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Cookie": f"LEETCODE_SESSION={session}; csrftoken={csrf_token}",
            "x-csrftoken": csrf_token,
            "Referer": "https://leetcode.com/",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        questions = data["data"]["problemsetQuestionList"]["questions"]
        return {q["titleSlug"]: q for q in questions}
    except Exception as e:
        print(f"Warning: could not fetch problem data ({e}). Using slug-derived titles, no difficulty.")
        return {}


def slug_to_title(slug: str) -> str:
    return " ".join(w.capitalize() for w in slug.split("-"))


def generate(session: str = "", csrf_token: str = "") -> None:
    problem_data = {}
    if session and csrf_token:
        problem_data = fetch_problem_data(session, csrf_token)

    entries = []
    for name in sorted(os.listdir(SUBMISSIONS_DIR)):
        path = os.path.join(SUBMISSIONS_DIR, name)
        if not os.path.isdir(path):
            continue
        m = re.match(r"^(\d+)-(.+)$", name)
        if not m:
            continue
        num = int(m.group(1))
        slug = m.group(2)

        meta = problem_data.get(slug, {})
        title = meta.get("title") or slug_to_title(slug)
        difficulty = meta.get("difficulty", "")

        langs = []
        for filename, label in [("solution.py", "py"), ("solution.java", "java")]:
            if os.path.exists(os.path.join(path, filename)):
                langs.append(f"[{label}]({SUBMISSIONS_DIR}/{name}/{filename})")
        solution_col = " ".join(langs) if langs else "—"

        entries.append((num, title, slug, difficulty, solution_col))

    lines = [
        "# LeetCode Submissions Index",
        "",
        f"{len(entries)} problems solved.",
        "",
        "| # | Title | Difficulty | Solution |",
        "|---|-------|------------|----------|",
    ]
    for num, title, slug, difficulty, solution_col in entries:
        lc_url = f"{LEETCODE_BASE}/{slug}/"
        lines.append(f"| {num} | [{title}]({lc_url}) | {difficulty} | {solution_col} |")
    lines.append("")

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(lines))
    print(f"Wrote {len(entries)} entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--session", default=os.environ.get("LEETCODE_SESSION", ""))
    parser.add_argument("--csrf-token", default=os.environ.get("LEETCODE_CSRF_TOKEN", ""))
    args = parser.parse_args()
    generate(session=args.session, csrf_token=args.csrf_token)
