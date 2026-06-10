# Limitations

The FindMyClient API has the following limitations to ensure stable, fair, and reliable usage for all users.

<br>

### :material-speedometer: Rate Limits
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.1</span>"

Requests are subject to rate limiting. Excessive usage may result in throttling or temporary delays.

!!! warning "Rate Limit Behavior"
    If limits are exceeded, the API will return a throttled response.

```json
{
  "error": "Too many requests. Please wait before trying again.",
  "status": "failed"
}
```

<br>

### :material-timer-sand: Asynchronous Processing
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.1</span>"

All requests are processed asynchronously.

After submitting a request, you must poll the result endpoint to retrieve the final output:

```http
/result/{job_id}
```
<br>

### :material-clock-outline: Processing Time
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.1</span>"

Processing time may vary depending on:

- Query complexity  
- Current system load  
- Availability of external data sources  

Some requests may complete quickly, while others may take longer depending on workload and crawling depth.

<br>

### :material-database-off: Data Availability
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.1</span>"

Results depend on publicly available data. In some cases:

- Business contact information may not exist  
- Email addresses may not be publicly accessible  
- Partial or incomplete results may be returned  

<br>

### :material-lan: Concurrent Requests
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.1</span>"

Concurrent request volume is limited to ensure system stability.

High parallel usage may result in:

- Request throttling  
- Increased latency  
- Delayed job processing  

<br>

### :material-check-circle-outline: Best Practices
=== "<span style='color: #6d82f6;'>:octicons-tag-24: 0.0.1</span>"

To ensure optimal performance:

- Use controlled request intervals  
- Avoid unnecessary parallel requests  
- Cache results when possible  
- Poll results with reasonable intervals (e.g., 10–60 seconds)

<br><br><br><br><br><br><br><br><br><br>