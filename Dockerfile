FROM python:3.8.7-slim-buster as base
RUN useradd -m service \
    && apt-get update \
    && apt-get install -y --no-install-recommends git gcc libc6-dev libgcc-8-dev \
    && apt-get install -y --reinstall build-essential \
    && pip install poetry \
    && su service -
WORKDIR /home/service

FROM base as prod
USER service
COPY --chown=service:service ./poetry.lock ./poetry.lock
COPY --chown=service:service ./pyproject.toml ./pyproject.toml
RUN poetry install --no-dev
COPY --chown=service:service . .
ENV WORKERS=3
USER service
CMD ["sh", "entrypoint.sh"]