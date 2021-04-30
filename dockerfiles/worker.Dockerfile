FROM python:3.8

COPY requirements.txt /


RUN pip3 install -r requirements.txt

COPY ./app /app


CMD ["/usr/local/bin/arq", "app.worker.WorkerSettings"]