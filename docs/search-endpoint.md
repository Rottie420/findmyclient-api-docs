# Getting Started

### :material-web: Base URL
---
```json
https://findmyclient.org/api
```
<br>

### :material-magnify: Search Endpoint
---

#### `POST` / `GET` `/search`

Submit a new search request.

!!! info "AI Agent Ready"

    The API returns structured JSON responses optimized for AI agents, automation systems, CRMs, and developer workflows.
<br>

### :material-code-json: POST Request
---

#### Endpoint

```http
  POST /search

```
#### Request Body

```json

{
  "query": "singapore cafe"
}

```

#### Example Request

```bash
curl -X POST "https://findmyclient.org/api/search" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "singapore cafe"
  }'
```
<br>

### :material-link-variant: GET Request
---

```http
GET /search?query=singapore+cafe&token=YOUR-API-TOKEN
```
#### Example Request

```bash
curl "https://findmyclient.org/api/search?query=singapore+cafe&token=YOUR-API-TOKEN"
```

<br>

### :material-database-search: Search Response
---

```json
{
  "credits_remaining": 4520,
  "job_id": "654e0e93-1a14-44d3-97e1-d7fabaf782fd",
  "status": "processing"
}
```
<br>

### :material-table: Response Fields
---

The following table describes the properties returned in the API response body.

| Field | Type | Description |
|---|---|---|
| `error` | string | Details regarding any syntax or processing errors encountered. |
| `status` | string | CuThe current execution state of the requested job. |
| `job_id` | string | Unique identifier assigned to the specific search job. |
| `credits_remaining` | int | The remaining balance of API credits available to the account. |
| `user` | string | The username or identifier associated with the active account. |

<br>

### :material-clock-outline: Async Processing
---

Search requests are processed asynchronously.

After submitting a search request, the API returns a `job_id` that can be used to track or retrieve results.

```json
{
  "job_id": "654e0e93-1a14-44d3-97e1-d7fabaf782fd",
  "status": "processing"
}
```


<br><br><br><br><br><br><br><br><br><br>