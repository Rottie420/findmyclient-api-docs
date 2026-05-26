# Getting Started

## Base URL

```json
https://findmyclient.org/api
```

## Result Endpoint

### `GET` `/result/<job_id>`

Retrieve the current status and results of a search job.

### Example

```json
/result/654e0e93-1a14-44d3-97e1-d7fabaf782fd
```

---

## Processing Response

Returned while the job is still running.

```json
{
  "created_at": "Sun, 24 May 2026 00:00:46 GMT",
  "error": null,
  "result": null,
  "status": "processing",
  "user": "user@test.com"
}
```

### Response Payload

The following table describes the properties returned in the API response body.

| Field | Type | Description |
| :--- | :--- | :--- |
| `created_at` | string (timestamp) | The date and time when the job was created, formatted in UTC. |
| `error` | string \| null | Details of any execution errors, or `null` if the operation is successful. |
| `result` | object \| null | The output payload of the completed job, or `null` if still in progress. |
| `status` | string | The current execution state of the requested job (e.g., `processing`). |
| `user` | string (email) | The email address associated with the account that initiated the request. |

---

## Completed Response

Returned once the search has completed successfully.

```json
{
  "created_at": "Sat, 23 May 2026 23:52:26 GMT",
  "credit_cost": 60,
  "error": null,
  "result": {
    "errors": [
      {
        "code": "crawl_failed",
        "count": 8,
        "retryable": true
      }
    ],
    "input": {
      "query": "singapore cafe"
    },
    "meta": {
      "agent": "findmyclient-email-scraper-v1",
      "execution_time_seconds": 26.57,
      "timestamp": "Sat, 23 May 2026 23:52:53 GMT"
    },
    "output": {
      "emails": [
        "asxvmprobertest@gmail.com",
        "events@mercimarcelgroup.com",
        "hello@mercimarcelgroup.com",
        "press@mercimarcelgroup.com",
        "smart.journey.prober@gmail.com",
        "work@mercimarcelgroup.com"
      ],
      "total_emails_found": 6,
      "total_failed_websites": 8,
      "total_websites_scanned": 10
    },
    "status": {
      "partial_failure": true,
      "success": true
    }
  },
  "status": "completed"
}
```
### Response Payload

The following table describes the properties returned in the API response body for a completed job.

| Field | Type | Description |
| :--- | :--- | :--- |
| `created_at` | string (timestamp) | The date and time when the job was initially created, formatted in UTC. |
| `credit_cost` | integer | The total number of API credits consumed by this operation. |
| `error` | string \| null | Global execution errors encountered at the job level, or `null` if the job completed processing. |
| `result` | object \| null | The root container for the scraped data payload and execution metrics. |
| `result.errors` | array (object) | A list of granular, non-fatal errors encountered during individual site crawls. |
| `result.errors[].code` | string | The specific error code identifier (e.g., `crawl_failed`). |
| `result.errors[].count` | integer | The total number of instances this specific error occurred during execution. |
| `result.errors[].retryable` | boolean | Indicates whether the failed operations can be retried. |
| `result.input` | object | The configuration and criteria parameters submitted with the original request. |
| `result.input.query` | string | The target search term or keywords used for the scraping job. |
| `result.meta` | object | Metadata related to the system execution and performance environment. |
| `result.meta.agent` | string | The identifier name and version of the scraper bot that executed the job. |
| `result.meta.execution_time_seconds` | float | The total time taken to process the job, measured in seconds. |
| `result.meta.timestamp` | string (timestamp) | The exact date and time when the processing was finalized. |
| `result.output` | object | The primary data payload extracted by the scraper. |
| `result.output.emails` | array (string) | A list of distinct, deduplicated email addresses uncovered during the search. |
| `result.output.total_emails_found` | integer | The total count of unique email addresses successfully extracted. |
| `result.output.total_failed_websites` | integer | The number of target websites that could not be successfully crawled. |
| `result.output.total_websites_scanned` | integer | The total number of unique web domains analyzed during the operation. |
| `result.status` | object | Internal health metrics for the specific dataset generation. |
| `result.status.partial_failure` | boolean | Flags whether some parts of the job failed (e.g., individual website timeouts) despite overall completion. |
| `result.status.success` | boolean | Indicates whether the core scraping engine successfully finished the processing run. |
| `status` | string | The top-level processing state of the request (e.g., `completed`). |


<br><br><br><br><br><br><br><br><br><br>