FROM python:3.8.7-slim-buster as base
RUN useradd -m service
WORKDIR /home/service

FROM base as builder
COPY ./requirements.txt ./
RUN apt-get update && apt-get install -y --no-install-recommends git gcc libc6-dev libgcc-8-dev \
    && apt-get install -y --reinstall build-essential \
    && su service - \
    && python -m venv venv \
    && venv/bin/pip install --no-cache-dir --upgrade pip \
    && venv/bin/pip install --no-cache-dir -r ./requirements.txt
USER service

FROM base as prod
COPY --chown=service:service ./project ./project
COPY --chown=service:service ./manage.py ./
COPY --chown=service:service ./entrypoint.sh ./
COPY --chown=service:service --from=builder /home/service/venv ./venv
ENV WORKERS=3
USER service
CMD ["sh", "entrypoint.sh"]