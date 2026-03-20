FROM python:3.11-slim 
ENV PYTHONUNBUFFERED=1 
WORKDIR /Authentication
COPY requirements.txt requirements.txt   
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /Authentication
EXPOSE 8000