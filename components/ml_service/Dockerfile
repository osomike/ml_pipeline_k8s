FROM python:3.8-slim

WORKDIR /app

# Copy files
COPY ./app/requirements.txt ./requirements.txt
COPY ./app/main.py ./main.py
COPY ./app/xgboost_classifier.pickle ./xgboost_classifier.pickle

# Install requirements
RUN apt-get update
RUN	apt-get install -y gcc vim
RUN pip install -r ./requirements.txt

# Only the last command will be executed
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
# docker build . -t k8s_ml_service_docker
# docker run -p 8000:8001 k8s_ml_service_docker