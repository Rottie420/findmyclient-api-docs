# Getting Started

## :material-web: Base URL

```json
https://findmyclient.org/api
```

---

## :material-magnify: Search Endpoint

### `POST` / `GET` `/search`

Submit a new search request.

!!! info "AI Agent Ready"

    The API returns structured JSON responses optimized for AI agents, automation systems, CRMs, and developer workflows.

---

### :material-code-json: POST Request

### Endpoint

```http
   POST /search

```
### Request Body

```json

{
  "query": "singapore cafe"
}

```

### GET Request

```json
/search?query=singapore+cafe&token=YOUR-API-TOKEN
```

---

## Search Response

```json
{
  "credits_remaining": 4520,
  "job_id": "654e0e93-1a14-44d3-97e1-d7fabaf782fd",
  "status": "processing"
}
```

### Response Payload

The following table describes the properties returned in the API response body.

| Field | Type | Description |
|---|---|---|
| `error` | string | Details regarding any syntax or processing errors encountered. |
| `status` | string | CuThe current execution state of the requested job. |
| `job_id` | string | Unique identifier assigned to the specific search job. |
| `credits_remaining` | int | The remaining balance of API credits available to the account. |
| `user` | string | The username or identifier associated with the active account. |

---


<br><br><br><br><br><br><br><br><br><br>