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
  "credits_remaining": 40,
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
  "created_at": "2026-05-15T13:51:31.928353",
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
  "credit_cost": 10,
  "created_at": "2026-05-15T13:51:31.928353",
  "error": null,
  "result": {
    "emails": [
      "asxvmprobertest@gmail.com",
      "cafedemusesg@gmail.com",
      "events@mercimarcelgroup.com",
      "hello@mercimarcelgroup.com",
      "jris@cafedemusesg.com",
      "press@mercimarcelgroup.com",
      "smart.journey.prober@gmail.com",
      "work@mercimarcelgroup.com"
    ],
    "failed_websites": 7,
    "query": "singapore cafe",
    "total_emails_found": 8,
    "total_websites": 10
  },
  "status": "completed"
}
```