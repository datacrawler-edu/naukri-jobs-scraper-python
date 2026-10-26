"""Combine three role and city searches in one bounded run."""
import json
from pathlib import Path
from client import collect

if __name__ == "__main__":
    payload = {"searches": [{"keyword": "software engineer", "location": "Bengaluru"},
                            {"keyword": "data analyst", "location": "Mumbai"},
                            {"keyword": "python developer", "location": "Pune"}],
               "maxJobs": 10, "sort": "relevance", "includeDetails": True, "includeCompanyDetails": True}
    items, complete = collect(payload)
    Path("naukri-batch.json").write_text(json.dumps(items, indent=2), encoding="utf-8")
    print(f"Saved {len(items)} jobs. Check SUMMARY for individual search coverage.")
    raise SystemExit(0 if complete else 2)
