# Getting Started

### :material-code-braces: Search Parameters

=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.8</span>"
The `/search` endpoint accepts the following parameters, either as query parameters or as a JSON body.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The search query used to find relevant websites and content. |
| `token` | string | Yes | Your API authentication token. |
| `max_pages` | integer | No | Maximum number of pages to crawl per website. Higher values allow deeper crawling at additional cost. |
| `max_websites` | integer | No | Maximum number of websites to include in the search. Costs scale with the number of websites beyond the included tier threshold. |
| `max_results` | integer | No | Maximum number of results to return in the response. |

### :material-language-python: Python Example

=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.8</span>"

```python
import requests

BASE_URL = "https://api.example.com"
API_TOKEN = "YOUR-API-TOKEN"
query = "Italy Winery"

response = requests.post(
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
```

!!! Notes

    - Omitted parameters fall back to default values defined by your account tier.
    - Increasing `max_websites` beyond the included threshold incurs additional cost per extra website.
    - `timeout` is a client-side setting and is not sent to the API.

<br><br><br><br><br><br><br><br><br><br>