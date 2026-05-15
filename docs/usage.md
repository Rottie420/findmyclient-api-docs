## Python

This example demonstrates how to interact with the FindMyClient API using a simple Python script. It shows the full workflow for executing an asynchronous search request, including job creation, polling, and result retrieval.

The process works in two steps:

1. Start a search job by sending a `POST` request to `/search,` which returns a `job_id`.
2. Poll the result endpoint `/result/{job_id}` until the job is completed and the final data is available.

This approach ensures efficient handling of long-running searches without blocking the system, making it suitable for automation tools, CLI scripts, and backend integrations.

Once the job status is marked as completed, the script returns structured business data extracted from the API.

```python

import requests
import time

BASE_URL = "https://findmyclient.org/api"


def search(query: str):
    # 1. Start search (POST request)
    response = requests.post(
        f"{BASE_URL}/search",
        json={"query": query},
        timeout=30
    )

    response.raise_for_status()
    data = response.json()

    job_id = data.get("job_id")
    print("Job started:", job_id)

    # 2. Poll result
    while True:
        result_url = f"{BASE_URL}/result/{job_id}"
        res = requests.get(result_url, timeout=30)
        res.raise_for_status()
        result = res.json()

        status = result.get("status")

        if status == "completed":
            return result["result"]

        print("Still processing...")
        time.sleep(2)


if __name__ == "__main__":
    output = search("singapore cafe")
    print("\nFinal Result:")
    print(output)



```

## cURL

You can interact with the FindMyClient API directly using `curl` for both starting a search and retrieving results.

Start a Search Job

```bash

curl -X POST "https://findmyclient.org/api/search" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "singapore cafe"
  }'


```
