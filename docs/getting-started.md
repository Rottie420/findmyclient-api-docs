# Getting Started

## Base URL

```txt
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

```txt
/api/search?query=singapore+cafe
```

---

## Response

```json
{
  "status": "processing",
  "job_id": "60a414d4-776b-4480-b6e1-ce541439cd51"
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

```txt
/api/result/60a414d4-776b-4480-b6e1-ce541439cd51
```

---

### Processing Response

Returned while the job is still running.

```json
{
  "status": "processing",
  "result": null
}
```

---

### Completed Response

Returned once the search has completed successfully.

```json
{
  "status": "completed",
  "result": {
    "query": "singapore cafe",
    "total_websites": 10,
    "total_emails_found": 3,
    "emails": [
      "contact@pscafe.com"
    ]
  }
}
```