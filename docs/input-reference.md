# Input reference

| Field | Default | Meaning |
|---|---|---|
| `searches` | Required | Array of 1–25 search objects. |
| `searches[].keyword` | Required | Non-empty role or skill phrase, up to 120 characters. |
| `searches[].location` | Empty | Indian city or region, up to 120 characters. Empty means all India. |
| `maxJobs` | 50 | Global limit of 1–1,000 unique jobs. |
| `sort` | `relevance` | `relevance` or `date`. |
| `includeDetails` | `true` | Request descriptions and available job details. |
| `includeCompanyDetails` | `true` | Request public company information. |

The sample requests five jobs. Earlier searches can fill the global limit before later searches run. Duplicate jobs are delivered once, with the search that first found them recorded. Invalid input types or a blank keyword stop collection with a message. The source may recognize common spelling variants; no automatic correction is guaranteed. Broadened searches are skipped and valid searches can continue.
