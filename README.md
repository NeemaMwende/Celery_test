# Agentic RAG

A FastAPI application with Redis Queue (RQ) for background job processing.

## Prerequisites

- Python 3.x
- Redis server
- Virtual environment (recommended)

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

### Terminal 1 - Start Redis

```bash
redis-server
```

### Terminal 2 - Start the FastAPI Server

```bash
uvicorn cron:app --reload
```

The API will be available at `http://localhost:8000`

### Terminal 3 - Start the RQ Worker

```bash
rq worker task_queue
```

The worker listens for jobs in the `task_queue` and executes them.

## API Endpoints

- `GET /` - Health check (returns `{"success": true, "message": "pong"}`)
- `POST /job` - Submit a job
  - Body: `{"lowest": 1, "highest": 10}`
  - Returns: `{"success": true, "job_id": "<job-id>"}`
- `GET /job/{job_id}` - Get job status and result
  - Returns: `{"status": "finished", "result": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}`

## Submitting a Job

```bash
curl -X POST http://localhost:8000/job \
  -H "Content-Type: application/json" \
  -d '{"lowest": 1, "highest": 10}'
```

## Viewing Logs

- **Uvicorn logs**: Shows API requests
- **RQ Worker logs**: Shows job processing output (logging.info messages from job.py)

## Stopping the Application

Press `Ctrl+C` in each terminal, or:

```bash
pkill -f "redis-server"
pkill -f "uvicorn"
pkill -f "rq worker"
```
