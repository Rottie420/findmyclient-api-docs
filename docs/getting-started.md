# Getting Started

## Base URL

```json
https://findmyclient.org/api
```

---

## Search Endpoint

### `POST` / `GET` `/search`

Submit a new search request.

### POST Request

```json
{
  "query": "singapore cafe"
}
```

### GET Request

```json
/api/search?query=singapore+cafe&token=YOUR-API-TOKEN
```

---

## Response

```json
{
  "credits_remaining": 4520,
  "job_id": "654e0e93-1a14-44d3-97e1-d7fabaf782fd",
  "status": "processing"
}
```

| Field | Type | Description |
|---|---|---|
| `status` | string | Current processing state |
| `job_id` | string | Unique identifier for the search job |

---

### Result Endpoint

### `GET` `/result/<job_id>`

Retrieve the current status and results of a search job.

### Example

```json
/api/result/654e0e93-1a14-44d3-97e1-d7fabaf782fd
```

---

### Processing Response

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

---

### Completed Response

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


<br><br><br><br><br><br><br><br><br><br>