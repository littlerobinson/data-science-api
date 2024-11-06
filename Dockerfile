FROM python:3.12.7-slim-bookworm

ENV MLFLOW_TRACKING_URI=$MLFLOW_TRACKING_URI

ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /code

RUN apt-get update & apt-get clean

COPY requirements.txt /dependencies/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /dependencies/requirements.txt

COPY ./app /code/app

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
# CMD gunicorn app.main:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker 