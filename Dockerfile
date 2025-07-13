FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry

COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root

# apiディレクトリごとコピー
COPY ./api /src/api

# モジュールルートを /src/api に設定
WORKDIR /src/api
ENV PYTHONPATH=/src/api

# uvicornの起動ポイントも合わせる
ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
