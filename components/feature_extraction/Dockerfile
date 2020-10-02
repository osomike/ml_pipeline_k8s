FROM python:3.8-slim

WORKDIR /app

# Copy files
COPY ./app/requirements.txt ./requirements.txt
COPY ./app/main.py ./main.py
COPY ./app/feature_engineering_lib.py ./feature_engineering_lib.py

# Install requirements
RUN apt-get update
RUN	apt-get install -y gcc vim
RUN pip install -r ./requirements.txt

# Only the last command will be executed
CMD ["python", "main.py", "{'raw_dir' : 'lalala', 'raw_input' : 25}"]
# docker build . -t k8s_feature_extraction_docker
# docker run k8s_feature_extraction_docker