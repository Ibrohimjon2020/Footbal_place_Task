FROM python:3.10.2-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .

RUN apt-get update -y && \
    apt-get install -y netcat && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD ./backend /code/backend
ADD ./devops /code/devops

RUN chmod +x /code/devops/backend/server-entrypoint.sh
# RUN chmod +x /code/devops/backend/worker-entrypoint.sh
RUN chmod +x /code/devops/backend/local-entrypoint.sh
# RUN chmod +x /code/devops/backend/flower-entrypoint.sh
