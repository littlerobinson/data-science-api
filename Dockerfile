FROM python:3.10.15-slim-bookworm

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV AWS_ARTIFACT_S3_URI=$AWS_ARTIFACT_S3_URI
ENV MLFLOW_TRACKING_URI=$MLFLOW_TRACKING_URI

ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /code

RUN apt-get update & apt-get clean

COPY requirements.txt /dependencies/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /dependencies/requirements.txt

COPY ./app /code/app

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
# CMD gunicorn app.main:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker 