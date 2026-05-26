# Getting Started

## Introduction

Welcome to the official documentation for FindMyClient API.

The API is built for asynchronous search processing. Each search request is queued as a background job and returns a unique `job_id`. You can retrieve results by polling the result endpoint until the job status is marked as `completed`.

Both **GET** and **POST** methods are supported for flexible integration with applications, scripts, and automation tools.

---


## Workflow Overview

The API follows a simple asynchronous workflow.

### 1. Submit Request

Call `/search` to create a new background search job.

### 2. Receive Job ID

The API immediately returns a unique `job_id`.

### 3. Check Status

Poll `/result/<job_id>` periodically to monitor progress.

### 4. Completion

Once the status becomes `completed`, retrieve the final search results.


<br><br><br><br><br><br><br><br><br><br>