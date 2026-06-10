# Getting Started

### :material-web: Base URL
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.1</span>"

```text
https://findmyclient.org/api
```
<br>

### :material-api: Result Endpoint
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.1</span>"

#### `GET` `/result/<job_id>`

Retrieve the current status and results of a search job.

#### Example Request

```http
GET /result/654e0e93-1a14-44d3-97e1-d7fabaf782fd
```
<br>

### :material-timer-sand: Processing Response
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.6</span>"

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
<br>

### :material-table: Response Fields (Processing)
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.6</span>"

| Field | Type | Description |
|------|------|-------------|
| `created_at` | string (timestamp) | When the job was created (UTC) |
| `error` | string \| null | Execution errors, or `null` if none |
| `result` | object \| null | Empty until job completes |
| `status` | string | Current job state (e.g. `processing`) |
| `user` | string (email) | Account that initiated the request |

<br>

### :material-check-circle: Completed Response
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.6</span>"

Returned once the job finishes successfully.

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
<br>

### :material-table: Response Fields (Completed)
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.6</span>"

#### Job Metadata

| Field | Type | Description |
|------|------|-------------|
| `created_at` | string (timestamp) | Job creation time (UTC) |
| `credit_cost` | integer | API credits used |
| `error` | string \| null | Global job error (if any) |
| `status` | string | Job state (e.g. `completed`) |


#### Result Object

| Field | Type | Description |
|------|------|-------------|
| `result` | object | Root container for extracted data |


#### Errors

| Field | Type | Description |
|------|------|-------------|
| `result.errors` | array | Non-fatal crawl errors |
| `result.errors[].code` | string | Error identifier (e.g. `crawl_failed`) |
| `result.errors[].count` | integer | Occurrence count |
| `result.errors[].retryable` | boolean | Whether retry is possible |


#### Input

| Field | Type | Description |
|------|------|-------------|
| `result.input.query` | string | Original search query |


#### Metadata

| Field | Type | Description |
|------|------|-------------|
| `result.meta.agent` | string | Scraper version used |
| `result.meta.execution_time_seconds` | float | Processing time |
| `result.meta.timestamp` | string | Completion timestamp |


#### Output Data

| Field | Type | Description |
|------|------|-------------|
| `result.output.emails` | array | Extracted email list |
| `result.output.total_emails_found` | integer | Unique emails found |
| `result.output.total_failed_websites` | integer | Failed website crawls |
| `result.output.total_websites_scanned` | integer | Total scanned domains |


#### Status Flags

| Field | Type | Description |
|------|------|-------------|
| `result.status.partial_failure` | boolean | Some sources failed but job completed |
| `result.status.success` | boolean | Overall success state |



<br><br><br><br><br><br><br><br><br><br>