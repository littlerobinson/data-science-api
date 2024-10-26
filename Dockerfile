FROM python:3.10.15-slim-bookworm

ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /code

RUN apt-get update & apt-get clean

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", $PORT]
# CMD ["uvicorn", "app/main.py", "--host", "0.0.0.0", "--port", $PORT]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", $PORT]
