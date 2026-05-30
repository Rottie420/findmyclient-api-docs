# Integration

### :material-connection: n8n Integration

Connect [FindMyClient.org](https://findmyclient.org) with n8n using the built-in HTTP Request node.

This integration is lightweight, flexible, and does not require a custom n8n community node. Since the FindMyClient API is REST-based, n8n can interact with it directly using standard HTTP requests.

<br>

### :material-sitemap: Workflow Overview
---

The integration follows a simple asynchronous workflow.

```mermaid
flowchart LR
    A[Client Request] --> B[POST /search]
    B --> C[Async Job Created]
    C --> D[Wait for Processing]
    D --> E[GET /result/{job_id}]
    E --> F[Final JSON Results]
```

<br>

### :material-play-circle-outline: Creating a Search Request
---

Add an **HTTP Request** node to your workflow.

#### Request Configuration

| Setting | Value |
|---|---|
| Method | `POST` |
| URL | `https://findmyclient.org/api/search` |

#### Headers

| Header | Value |
|---|---|
| token | `YOUR_API_TOKEN` |
| Content-Type | `application/json` |


#### Request Body

```json
{
  "query": "restaurants in singapore"
}
```

#### Example Response

After submitting the request, the API returns a processing response containing a `job_id`.

```json
{
  "job_id": "job_abc123",
  "status": "processing"
}
```

<br>

### :material-timer-sand: Waiting for Processing
---

Because searches are processed asynchronously, it is recommended to add a **Wait** node after the initial request.

!!! info "Recommended Delay"
    A delay between **5–10 seconds** is usually sufficient for standard searches.

This reduces unnecessary polling and helps minimize API load.

<br>

### :material-database-search: Fetching Results
---

Add a second **HTTP Request** node to retrieve the completed result.

| Setting | Value |
|---|---|
| Method | `GET` |
| URL | `https://findmyclient.org/api/result/{{$json.job_id}}` |

Use the same authorization header from the initial request.

<br>

#### Example Result

```json
{
  "status": "completed",
  "result": {
    "email": []
  }
}
```

<br>

### :material-source-branch: Typical Workflow
---

A common production workflow looks similar to the example below.

```mermaid
flowchart LR
    A[Webhook Trigger]
    --> B[HTTP POST /search]
    --> C[Wait Node]
    --> D[HTTP GET /result/{job_id}]
    --> E[CRM / Spreadsheet / AI Agent]
```

This structure works well for:

- CRM enrichment  
- AI prospecting systems  
- Outbound automation  
- Internal lead research workflows  

<br>

### :material-shield-check-outline: Production Recommendations
---

For larger workflows:

- Store returned `job_id` values for retry handling  
- Use environment variables for API credentials  
- Add retry logic for failed requests  
- Implement rate limiting for high-volume workflows  
- Cache repeated searches where possible  

<br>

### :material-apps: Integration Ideas
---

FindMyClient can integrate with:

- HubSpot  
- Google Sheets  
- Airtable  
- Notion  
- Slack  
- Discord  
- Internal CRM systems  

Many teams also combine FindMyClient with AI agents to automate:

- Prospect qualification  
- Company research  
- Lead enrichment  
- Outbound workflows  

<br>

### :material-rocket-launch-outline: Next Steps
---

Once your integration is working, reusable n8n templates can be created for:

- CRM enrichment  
- Automated prospect discovery  
- AI-powered lead qualification  
- Internal business workflows  

This helps standardize automation pipelines and accelerate deployment across teams.

<br><br><br><br><br><br><br><br><br><br>