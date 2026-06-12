---
icon: material/fire
---

# Getting Started

### :material-web: Base URL
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.1</span>"

```text
https://findmyclient.org/api
```

<br>

### :material-api: Enriched Leads Endpoint
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.7</span>"

#### `GET` `/result/leads/<job_id>`

Retrieve enriched and processed leads generated from a completed job.

This endpoint provides validated, classified, and confidence-scored lead data derived from the original scraping output.

#### Example Request

```http
GET /result/leads/654e0e93-1a14-44d3-97e1-d7fabaf782fd
```

<br>

### :material-sync: Client Workflow Integration

=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.7</span>"

The client workflow automatically handles job completion and lead retrieval:

* Poll `/result/<job_id>` until status is `completed`
* Once completed, fetch enriched data from `/result/leads/<job_id>`
* Downstream systems consume only the enriched lead dataset

This removes the need for manual post-processing of raw scraping results.

<br>


### :material-check-decagram: Enriched Leads Response (Leads Endpoint)

=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.7</span>"

Returned after enrichment processing is applied to completed jobs.

```json
{
  "rows": [
    {
      "email": "info@cafeexample.com",
      "domain": "cafeexample.com",
      "email_type": "role",
      "confidence_score": 0.82,
      "is_valid": true,
      "source": "website_crawl"
    },
    {
      "email": "john@business.com",
      "domain": "business.com",
      "email_type": "personal",
      "confidence_score": 0.94,
      "is_valid": true,
      "source": "website_crawl"
    }
  ],
}
```

<br>

### :material-table: Response Fields (Enriched Leads)

=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.7</span>"

#### Lead Object

| Field              | Type    | Description                                    |
| ------------------ | ------- | ---------------------------------------------- |
| `email`            | string  | Extracted email address                        |
| `domain`           | string  | Email domain                                   |
| `email_type`       | string  | Classification (`personal`, `role`, `generic`) |
| `confidence_score` | float   | Lead quality score (0–1)                       |
| `is_valid`         | boolean | Whether email passed validation                |
| `source`           | string  | Origin of the email (e.g. `website_crawl`)     |

<br>

#### Summary Object

| Field                         | Type    | Description                             |
| ----------------------------- | ------- | --------------------------------------- |
| `summary.total_leads`         | integer | Total enriched leads                    |
| `summary.valid_leads`         | integer | Valid leads after filtering             |
| `summary.role_based_filtered` | integer | Role-based emails removed or downgraded |


### :material-language-python: Python Example

=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.8</span>"

```python
import time
import requests

BASE_URL = "http://127.0.0.1:5000/api"
API_TOKEN = "YOUR-API-TOKEN"


def search(query: str):
    # 1. Start job
    res = requests.post(
        f"{BASE_URL}/search",
        params={
            "query": query,
            "token": API_TOKEN,
            "max_pages": 20,
            "max_websites": 20,
            "max_results": 20,
        },
        timeout=30,
    )
    res.raise_for_status()
    job_id = res.json()["job_id"]

    print("Job started:", job_id)

    # 2. Poll status
    while True:
        res = requests.get(f"{BASE_URL}/result/{job_id}", timeout=30)
        res.raise_for_status()
        data = res.json()

        print("Status:", data.get("status"))

        if data.get("status") == "completed":
            if data.get("error"):
                raise Exception(data["error"])
            break

        if data.get("status") == "failed":
            raise Exception(data.get("error", "Job failed"))

        # waiting for response to avoid rate-limit.
        time.sleep(30)  

    # 3. Get results
    res = requests.get(f"{BASE_URL}/result/leads/{job_id}", timeout=30)
    res.raise_for_status()

    return res.json()


if __name__ == "__main__":
    result = search("singapore cafe")

    for row in result.get("rows", []):
        print(row)
```

<br><br><br><br><br><br><br><br><br><br>
