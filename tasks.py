# from celery import Celery
# from time import sleep

# app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')

# @app.task
# def process(x, y):
#     i = 0 
#     while i < 5:
#         sleep(1)
#         i += 1
#         (print("Processing..."))
        
#     return x**2 + y**2 





from celery import Celery
import time

app = Celery('tasks', broker='redis://localhost:6379')

@app.task
def send_email(email):
    print(f"Sending email to {email}...")
    time.sleep(5)
    print("Done!")
