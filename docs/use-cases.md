# Integration workflows

## Find jobs for a role and city

Use `examples/python/collect_jobs.py` for five software engineer jobs in Bengaluru. The cap is a maximum, not a promise that the source has that many matches.

## Combine several cities and roles

Use `examples/python/batch_searches.py` for Bengaluru, Mumbai and Pune with a global ten-job cap. This is not an equal-size city sample: earlier searches can fill the cap. Use separate runs when each city needs an independent quota.

## Export existing jobs to a spreadsheet

Use `examples/python/export_jobs_csv.py DATASET_ID` to read up to 1,000 existing rows. No collection starts. The CSV selects title, company, location, salary, experience and job link. Spreadsheet formula-like cells are escaped.

## Explore salary labels and skills

Analyze the returned salary text and skills array in your own workflow. Unavailable salaries remain unavailable. Applicant profiles and job applications are outside this Actor's scope.
