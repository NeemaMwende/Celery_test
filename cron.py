from fastapi import FastAPI 
from redis import Redis 
from rq import Queue
from pydantic import BaseModel
from job import print_number

app = FastAPI()
redis_conn = Redis(host="localhost", port=6379)
task_queue = Queue("task_queue", connection=redis_conn)

class JobData(BaseModel):
    lowest: int 
    highest: int 
    
    
@app.get("/")
def index():
    return {
        "success": True,
        "message": "pong"
    }
    
# create the job 
@app.post("/job")
def post_job(job: JobData):
    lowest = job.lowest
    highest = job.highest 
    job_instance = task_queue.enqueue(print_number, lowest, highest)
    return{
        "success": True,
        "job_id": job_instance.id
    }
    
@app.get("/job/{job_id}")
def get_job_result(job_id: str):
    job = Job.fetch(job_id, connection=redis_conn)
    return {"status": job.get_status(), "result": job.result}
