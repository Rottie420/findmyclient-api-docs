## Python

This example demonstrates how to interact with the FindMyClient API using a simple Python script. It shows the full workflow for executing an asynchronous search request, including job creation, polling, and result retrieval.

The process works in two steps:

1. Start a search job by sending a `POST` request to `/search,` which returns a `job_id`.
2. Poll the result endpoint `/result/{job_id}` until the job is completed and the final data is available.

This approach ensures efficient handling of long-running searches without blocking the system, making it suitable for automation tools, CLI scripts, and backend integrations.

Once the job status is marked as completed, the script returns structured business data extracted from the API.

```python

import time

import requests

BASE_URL = "https://findmyclient.org/api"
API_TOKEN = "YOUR-API-TOKEN"


def search(query: str):

    # Start search
    response = requests.get(
        f"{BASE_URL}/search", params={"query": query, "token": API_TOKEN}, timeout=30
    )

    response.raise_for_status()

    data = response.json()
    job_id = data["job_id"]
    print(f"Job started: {job_id}")

    # Poll results
    while True:

        result = requests.get(f"{BASE_URL}/result/{job_id}", timeout=30)
        result.raise_for_status()
        payload = result.json()
        status = payload["status"]

        if status == "completed":

            if payload["error"]:
                raise Exception(payload["error"])

            return payload["result"]

        print("Still processing...")

        time.sleep(60)


if __name__ == "__main__":

    output = search("singapore cafe")
    print("\nFinal Result:\n")
    print(output)



```

## cURL

You can interact with the FindMyClient API directly using `curl` for both starting a search and retrieving results.

Start a Search Job

macOS / Linux (bash)

```bash

curl -X POST "https://findmyclient.org/api/search" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "singapore cafe"
  }'

```
<br>

Windows (CMD)

```cmd

curl -X POST "https://findmyclient.org/api/search" -H "Authorization: Bearer YOUR_API_TOKEN" -H "Content-Type: application/json" -d "{\"query\":\"singapore cafe\"}"

```
<br>

Windows (PowerShell)

```PowerShell

Invoke-RestMethod -Method POST `
  -Uri "https://findmyclient.org/api/search" `
  -Headers @{Authorization="Bearer YOUR_API_TOKEN"} `
  -Body (@{query="singapore cafe"} | ConvertTo-Json)

```

<br><br><br><br><br><br><br><br><br><br>
