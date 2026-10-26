# FAQ

## Do I need a Naukri account?

No. The hosted Actor collects public jobs. API examples require your Apify token and live collection can incur charges.

## Is this an official Naukri API?

No. These examples call the hosted Apify Actor.

## Can I use several search terms and cities?

Yes: up to 25 search entries share one global cap of up to 1,000 unique jobs. The row records the query that first found a job.

## What happens with spelling mistakes?

Common variants may be recognized by the source. The Actor does not invent corrections. If a search is broadened, its unrelated results are skipped. Blank location intentionally means all India.

## Are all jobs or full details guaranteed?

No. Source availability, matching jobs, limits and missing public fields affect coverage. Review the summary and per-row detail status. A missing summary means unknown coverage.

## What does it cost?

One event is charged per unique delivered job. Tier prices range from $0.75 to $1.00 per 1,000 jobs. Check the [live Pricing tab](https://apify.com/datascraperes/naukri-jobs-scraper?fpr=edudata). Example starts cap Actor charges at $0.01; platform charges may apply separately. Exporting an existing Dataset starts no new collection or job-result events.

## Is the sample output complete?

It is a selected-field projection from a real public job row, not the entire output schema or a guarantee the listing remains live.
