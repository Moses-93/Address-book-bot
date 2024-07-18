FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /web_hw_m2

COPY . /web_hw_m2

RUN poetry install --no-root

CMD [ "python", "main.py" ]