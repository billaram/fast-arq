docker build -f ./dockerfiles/app.Dockerfile -t billaram/fast-arq-app:latest .
docker build -f ./dockerfiles/worker.Dockerfile -t billaram/fast-arq-worker:latest .
