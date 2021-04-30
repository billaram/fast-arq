
# EXAMPLE FAST API AND ASYNC TASK QUEUE APP

## REQUIREMENTS 

* fastapi
* arq
* docker
* docker-compose

## USAGE

* clone the repo

```
docker-compose up -d
```

* to trigger the async notfication task

```
curl http://localhost:8080/api/notif/
```

## APP 

* The app runs the notification process in the backgroud as the async task with redis backend for queuing

e.g the following api `[GET] /api/notif` triggers notif task and the task will get executed in the arq worker in the background