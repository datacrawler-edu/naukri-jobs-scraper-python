# Naukri Jobs Scraper: Python API and CSV Examples

Search public India jobs by keyword and city using [Naukri Jobs Scraper](https://apify.com/datascraperes/naukri-jobs-scraper?fpr=edudata). This guide contains hosted API examples, a no-code walkthrough and an existing-Dataset CSV export.

## What this repository helps you do

- Find jobs by role and Indian city.
- Combine role/city searches with one global cap.
- Read available salary, experience, skills and company data.
- Export existing results without collecting them again.

## Example result

The [sample JSON](data/sample-output.json) is a selected-field projection from a real job. The [sample CSV](data/sample-output.csv) contains spreadsheet columns. Live listings can change.

```json
{
  "recordType": "job",
  "jobId": "261026005898",
  "title": "Software Engineer",
  "companyName": "Qualcomm",
  "location": "Bengaluru",
  "experience": "0-1 Yrs",
  "salary": "17-32 Lacs",
  "skills": [
    "C++",
    "Python"
  ],
  "jobUrl": "https://www.naukri.com/job-listings-software-engineer-qualcomm-bengaluru-0-to-1-years-261026005898",
  "searchKeyword": "software engineer",
  "searchLocation": "Bengaluru",
  "searchPage": 1,
  "detailStatus": "complete",
  "scrapedAt": "2026-10-26T14:40:59.301405+00:00"
}
```

## Run without code

1. Open [Naukri Jobs Scraper on Apify](https://apify.com/datascraperes/naukri-jobs-scraper?fpr=edudata).
2. In **Input**, add a keyword and optional city to **Job searches**.
3. Set **Maximum unique jobs** to 5 and click **Start**.
4. Inspect **Dataset**, then export JSON, CSV or Excel.

See the [no-code guide](docs/no-code-guide.md). You need an Apify account; no Naukri login is required.

## Try it with Apify's free plan

Apify's Free plan includes **$5 in monthly prepaid usage**, with no credit card required to start. Credit can cover a small first collection; usage is not unlimited. Unused credits expire at the end of the billing cycle. See [current Apify pricing](https://apify.com/pricing?fpr=edudata).

## Quick start for developers

Use Python 3.11+; the examples use the standard library.

```bash
export APIFY_API_TOKEN="your-token"
python examples/python/collect_jobs.py
```

Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
python examples/python/collect_jobs.py
```

This starts a chargeable run with five jobs maximum, a five-minute server timeout and a $0.01 Actor-charge cap. The client polls, checks the summary and writes available rows to `naukri-jobs.json`. Exit code 2 means complete coverage could not be confirmed. After a lost start acknowledgement, inspect Console before repeating the POST.

## Input example

```json
{
  "searches": [
    {
      "keyword": "software engineer",
      "location": "Bengaluru"
    }
  ],
  "maxJobs": 5,
  "sort": "relevance",
  "includeDetails": true,
  "includeCompanyDetails": true
}
```

See the [input reference](docs/input-reference.md). Blank location means all India; a non-empty keyword is required.

## Request examples

- [cURL requests](examples/curl-request.md): start, inspect status and download.
- [Python single run](examples/python/collect_jobs.py): bounded five-job sample.
- [Python multiple searches](examples/python/batch_searches.py): roles and cities.
- [Python CSV export](examples/python/export_jobs_csv.py): existing Dataset only.
- [JavaScript](examples/javascript/request.mjs): Node.js 20+, run `node examples/javascript/request.mjs`.

## Output fields

| Field | Meaning |
|---|---|
| `jobId`, `jobUrl` | Source identity and public job link. |
| `title`, `companyName`, `location` | Job, employer and advertised location. |
| `salary`, `experience`, `skills` | Available salary text, experience text and skill list. |
| `description`, `companyRating` | Optional description and company information. |
| `detailStatus` | Coverage of requested job details. |
| `searchKeyword`, `searchLocation` | Search that first found this job. |

See the [output reference](docs/output-reference.md). Missing public information remains missing.

## Common use cases

See [workflows](docs/use-cases.md) for role sourcing, city comparisons, skills research and spreadsheet exports.

## Search Naukri jobs across several Indian cities with Python

Run `python examples/python/batch_searches.py`. It combines three searches under a global ten-job cap, rather than ten jobs per city. Earlier searches may fill the cap. Use separate runs for independent city quotas.

## Export an existing Naukri jobs Dataset to CSV

```bash
python examples/python/export_jobs_csv.py DATASET_ID --output naukri-jobs.csv
```

The export reads at most 1,000 existing rows. It starts no new collection. Its count is not a guarantee of all available source jobs. Spreadsheet formula-like values are escaped.

## FAQ

The [FAQ](docs/faq.md) covers spelling, empty results, missing data and costs. If the source broadens a query, unrelated results are skipped; other valid searches can continue. A platform SUCCEEDED status alone does not prove complete collection: inspect SUMMARY.

## Limits and pricing

Up to **25 searches** share a **1–1,000 unique-job cap**. Default cap: 50; sample cap: 5. Detail and company fields depend on public availability. Reaching your cap does not mean every source job was collected.

Pricing is **pay per event**, once per unique delivered job:

| Apify tier | Per job result | Per 1,000 results |
|---|---:|---:|
| Free | $0.001 | $1.00 |
| Bronze | $0.0009 | $0.90 |
| Silver | $0.0008 | $0.80 |
| Gold, Platinum, Diamond | $0.00075 | $0.75 |

Verify the [live Actor Pricing tab](https://apify.com/datascraperes/naukri-jobs-scraper?fpr=edudata) before larger runs. Empty or skipped searches produce no delivered-job events. Example budgets cap Actor charges; other platform/account charges may apply separately.

## Hosted version

[Run Naukri Jobs Scraper on Apify](https://apify.com/datascraperes/naukri-jobs-scraper?fpr=edudata) for hosted execution, stored results and API access. This repository contains client examples, not a locally running collector. Links using `fpr=edudata` are affiliate links; we may receive a referral commission.

## Responsible use

Use public data lawfully and respect applicable terms and privacy obligations. Never commit your token. Applicant data and automatic job applications are outside this guide.

## Support

[Open a GitHub issue](https://github.com/datacrawler-edu/naukri-jobs-scraper-python/issues) for integration example problems. For collection problems, use the hosted Actor's Issues tab. Include sanitized input and run ID, never credentials.

## License

Documentation and examples are provided under the [MIT License](LICENSE).
