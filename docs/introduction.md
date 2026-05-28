# Getting Started

### :material-book-open-page-variant: Introduction
---

Welcome to the official documentation for the FindMyClient API.

The API is built for asynchronous search processing. Each search request is queued as a background job and returns a unique `job_id`. You can retrieve results by polling the result endpoint until the job status is marked as `completed`.

Both **GET** and **POST** methods are supported for flexible integration with applications, scripts, AI agents, and automation workflows.

<br>

!!! info "Async Processing"

    Search requests are processed in the background to support scalable business discovery and large web data operations.

<br>

### :material-source-branch: Workflow Overview
---

The API follows a simple asynchronous workflow.

```bash
flowchart LR
    A[Submit Search Request] --> B[Receive job_id]
    B --> C[Poll Result Endpoint]
    C --> D[Status Completed]
    D --> E[Retrieve Results]
```

<br>

### :material-numeric-1-circle: Submit Request
---

Call the `/search` endpoint to create a new background search job.

```http
POST /search
```

<br>

### :material-numeric-2-circle: Receive Job ID
---

The API immediately returns a unique `job_id`.

```json
{
  "job_id": "654e0e93-1a14-44d3-97e1-d7fabaf782fd",
  "status": "processing"
}
```

<br>

### :material-numeric-3-circle: Check Status
---

Poll the result endpoint periodically to monitor progress.

```http
GET /result/<job_id>
```

Example:

```http
GET /result/654e0e93-1a14-44d3-97e1-d7fabaf782fd
```
<br>

### :material-numeric-4-circle: Completion
---

Once the status becomes `completed`, retrieve the final search results.

```json
{
  "status": "completed",
  "result": {
    "emails": []
  }
}
```
<br>

### :material-robot-outline: Designed For
---

FindMyClient is designed for:

- AI agents
- CRM enrichment
- Internal lead generation systems
- Workflow automation
- n8n pipelines
- Business intelligence tools
- Developer integrations

<br><br><br><br><br><br><br><br><br><br>