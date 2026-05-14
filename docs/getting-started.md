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

```json
/api/result/60a414d4-776b-4480-b6e1-ce541439cd51
```

---

### Processing Response

Returned while the job is still running.

```json
{
  "created_at": "2026-05-14T09:49:32.857753",
  "error": null,
  "result": null,
  "status": "processing"
}
```

---

### Completed Response

Returned once the search has completed successfully.

```json
{
  "created_at": "2026-05-14T09:49:32.857753",
  "error": null,
  "result": {
    "emails": [
      "contact@pscafe.com",
      "franck@myawesomecafe.com"
    ],
    "failed_websites": 8,
    "query": "singapore cafe",
    "total_emails_found": 2,
    "total_websites": 10
  },
  "status": "completed"
}
```