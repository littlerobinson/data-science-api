FROM python:3.10.15-slim-bookworm

ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /code

RUN apt-get update & apt-get clean

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 4000

CMD ["fastapi", "run", "app/main.py", "--port", "80"]