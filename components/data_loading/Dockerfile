FROM python:3.8-slim

WORKDIR /app

# Copy files
COPY ./app/requirements.txt ./requirements.txt
COPY ./app/main.py ./main.py
COPY ./app/load_data_lib.py ./load_data_lib.py
COPY ./app/data.json ./data.json

# Install requirements
RUN apt-get update
RUN	apt-get install -y gcc vim
RUN pip install -r ./requirements.txt

# Only the last command will be executed
CMD ["python", "main.py"]
# docker build . -t k8s_data_loading_docker
# docker run k8s_data_loading_docker