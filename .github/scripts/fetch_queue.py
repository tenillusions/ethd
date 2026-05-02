#!/usr/bin/env python3
"""Fetch and parse validatorqueue.com data into JSON for GitHub Pages."""

import json
import re
import sys
import urllib.request

def fetch_page():
    req = urllib.request.Request(
        "https://www.validatorqueue.com",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8")

def parse(html):
    result = {"updatedAt": None}

    # historical data
    m = re.search(r"const\s+historical_data\s*=\s*(\[[\s\S]*?\])\s*[;\n]", html)
    if m:
        try:
            result["historical"] = json.loads(m.group(1))
        except json.JSONDecodeError:
            pass

    # The HTML wraps values in <span> tags: <span>Label: </span><span>Value</span>
    sp = r"[\s\S]{0,800}?"
    patterns = {
        "entry": r"Entry Queue" + sp + r"ETH:\s*</span>\s*<span>([\d,]+)",
        "entryWait": r"Entry Queue" + sp + r"Wait:\s*</span>\s*<span>([\d]+ days?,?\s*[\d]+ hours?)",
        "entryChurn": r"Entry Queue" + sp + r"Churn:\s*</span>\s*<span>([\d/epoch]+)",
        "exit": r"Exit Queue" + sp + r"ETH:\s*</span>\s*<span>([\d,]+)",
        "exitWait": r"Exit Queue" + sp + r"Wait:\s*</span>\s*<span>([\d]+ days?,?\s*[\d]+ hours?)",
        "exitChurn": r"Exit Queue" + sp + r"Churn:\s*</span>\s*<span>([\d/epoch]+)",
        "sweep": r"Sweep Delay" + sp + r"([\d.]+ days?)",
        "validators": r"Active Validators:\s*</span>\s*<span>([\d,]+)",
        "staked": r"Staked ETH:\s*</span>\s*<span>([\d.]+[MBK]?)\s*\(([\d.]+%)\)",
        "apr": r"APR:\s*</span>\s*<span>([\d.]+%)",
    }

    for key, pattern in patterns.items():
        m = re.search(pattern, html, re.IGNORECASE)
        if m:
            if key == "staked":
                result["staked"] = m.group(1)
                result["stakedPct"] = m.group(2)
            else:
                result[key] = m.group(1)

    if not result.get("entry"):
        print("ERROR: could not parse entry queue data", file=sys.stderr)
        sys.exit(1)

    return result

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = fetch_page()
    data = parse(html)
    data["updatedAt"] = datetime.now(timezone.utc).isoformat()
    with open("queue-data.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote queue-data.json (entry={data.get('entry')}, exit={data.get('exit')})")
