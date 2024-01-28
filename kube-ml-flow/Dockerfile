FROM python:3.11-slim-buster

RUN pip3 install --upgrade pip && \
    pip3 install mlflow==1.20.2 boto3 psycopg2-binary


ENTRYPOINT ["mlflow"," server"]