# Celery_test

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

---

# Authentication Project

A FastAPI application with GraphQL, PostgreSQL, Redis, Celery, and Flower for user authentication and task processing.

## Prerequisites

- Docker and Docker Compose
- Python 3.11+ (handled by Docker)

## Running the Application

### Start all services

```bash
cd Authentication
docker compose up -d
```

This will start:
- **PostgreSQL** (database) - Port 5432
- **Redis** (message broker) - Port 6379
- **PGAdmin** (database management) - Port 5050
- **App** (FastAPI server) - Port 8000
- **Celery Worker** (background tasks)
- **Flower** (Celery monitoring) - Port 5556

## URLs

| Service | URL |
|---------|-----|
| FastAPI App | http://localhost:8000 |
| GraphQL Playground | http://localhost:8000/graphql |
| PGAdmin | http://localhost:5050 |
| Flower (Celery Monitor) | http://localhost:5556 |

## Default Credentials

### PGAdmin
- Email: admin@admin.com
- Password: admin

### PostgreSQL
- Host: db
- Port: 5432
- User: postgres
- Password: admin
- Database: post_db

## Environment Variables

Create a `.env` file in the `Authentication` folder:

```env
DATABASE_URL=postgresql+psycopg2://postgres:admin@db:5432/post_db
DB_USER=postgres
DB_PASSWORD=admin
DB_NAME=post_db
PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin
SECRET_KEY=your-secret-key
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

## Docker Commands

```bash
# Start services
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs app
docker compose logs celery_worker

# Rebuild after changes
docker compose build
docker compose up -d
```

## API Endpoints (GraphQL)

The app uses GraphQL at `/graphql`. Example queries:

```graphql
# Create a new user
mutation {
  createNewUser(username: "testuser", password: "password123") {
    ok
  }
}

# Authenticate user
mutation {
  authenticateUser(username: "testuser", password: "password123") {
    ok
    token
  }
}

# Get all posts
query {
  allPosts {
    id
    title
    content
  }
}

# Create a post (requires token)
mutation {
  createNewPost(title: "My Post", content: "Content here", token: "YOUR_JWT_TOKEN") {
    result
  }
}
```