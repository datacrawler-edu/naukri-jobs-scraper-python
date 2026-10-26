# Output reference

One row represents one unique job. Fields may be absent or null when public information is unavailable. The sample is a projection from a real row.

| Field | Type |
|---|---|
| `recordType` | string |
| `jobId` | string |
| `title` | string or null |
| `companyName` | string or null |
| `companyId` | integer or null |
| `groupId` | integer or null |
| `companyLogo` | string or null |
| `companyRating` | number or null |
| `companyReviewsCount` | integer or null |
| `companyTags` | array |
| `companyIndustry` | string or null |
| `companyProfileUrl` | string or null |
| `location` | string or null |
| `locations` | array |
| `experience` | string or null |
| `minimumExperience` | integer or null |
| `maximumExperience` | integer or null |
| `salary` | string or null |
| `salaryMin` | integer or null |
| `salaryMax` | integer or null |
| `salaryCurrency` | string or null |
| `salaryHidden` | boolean or null |
| `skills` | array |
| `description` | string or null |
| `descriptionHtml` | string or null |
| `shortDescription` | string or null |
| `jobType` | string or null |
| `employmentType` | string or null |
| `workFromHomeType` | string or null |
| `roleCategory` | string or null |
| `jobRole` | string or null |
| `functionalArea` | string or null |
| `industry` | string or null |
| `education` | object or null |
| `vacancy` | integer or null |
| `applyCount` | integer or null |
| `viewCount` | integer or null |
| `postedDate` | string or null |
| `jobUrl` | string or null |
| `applyUrl` | string or null |
| `searchKeyword` | string or null |
| `searchLocation` | string or null |
| `searchPage` | integer or null |
| `detailStatus` | string |
| `companyDetailStatus` | string or null |
| `scrapedAt` | string |

`jobId` identifies the job and `jobUrl` links to it. Query provenance is recorded by `searchKeyword`, `searchLocation` and `searchPage`. `detailStatus` can distinguish complete, listing-only, batch-only or failed detail coverage. `companyDetailStatus` describes optional company data.

Read SUMMARY too. `completed` and `empty` differ from `partial`, `search_not_matched`, `source_unavailable`, `invalid_input`, `time_limit` or `charge_limit`. Preserve available rows on a partial run. A missing summary means unknown coverage.
