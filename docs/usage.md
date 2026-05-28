# Basic Usage

This example demonstrates how to interact with the FindMyClient API using Python.

It covers the full asynchronous workflow:
- Create a search job
- Poll for completion
- Retrieve final results

This approach is ideal for automation scripts, backend systems, and AI agent integrations.

<br>

### :material-language-python: Python Example
---

```python
import time
import requests

BASE_URL = "https://findmyclient.org/api"
API_TOKEN = "YOUR-API-TOKEN"


def search(query: str):
    # Start search job
    response = requests.post(
        f"{BASE_URL}/search",
        params={"query": query, "token": API_TOKEN},
        timeout=30
    )

    response.raise_for_status()
    data = response.json()

    job_id = data["job_id"]
    print(f"Job started: {job_id}")

    # Poll for results
    while True:
        result = requests.get(
            f"{BASE_URL}/result/{job_id}",
            timeout=30
        )

        result.raise_for_status()
        payload = result.json()
        status = payload["status"]

        if status == "completed":
            if payload.get("error"):
                raise Exception(payload["error"])

            return payload["result"]

        print("Still processing...")
        time.sleep(60)


if __name__ == "__main__":
    output = search("singapore cafe")
    print("\nFinal Result:\n")
    print(output)
```

<br>

### :material-console: cURL
---

You can also interact with the API directly using `curl`.

<br>

### :material-play: Start a Search Job
---

#### macOS / Linux (bash)

```bash
curl -X POST "https://findmyclient.org/api/search" \
  -H "token: YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "singapore cafe"
  }'
```
<br>

#### Windows (CMD)

```cmd
curl -X POST "https://findmyclient.org/api/search" -H "token: YOUR_API_TOKEN" -H "Content-Type: application/json" -d "{\"query\":\"singapore cafe\"}"
```
<br>

#### Windows (PowerShell)

```powershell
Invoke-RestMethod -Method POST `
  -Uri "https://findmyclient.org/api/search" `
  -Headers @{token="YOUR_API_TOKEN"} `
  -Body (@{query="singapore cafe"} | ConvertTo-Json)
```
<br>

### :material-database: Get Results
---

#### macOS / Linux (bash)

```bash
curl -X GET "https://findmyclient.org/api/result/YOUR_JOB_ID"
```

<br>>

#### Windows (CMD)

```cmd
curl -X GET "https://findmyclient.org/api/result/YOUR_JOB_ID"
```

<br>

#### Windows (PowerShell)

```powershell
Invoke-RestMethod -Method GET `
  -Uri "https://findmyclient.org/api/result/YOUR_JOB_ID"
```

<br><br><br><br><br><br><br><br><br><br>