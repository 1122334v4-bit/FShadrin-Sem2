FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim
WORKDIR /app

RUN useradd --create-home --uid 1000 appuser

COPY --from=builder /install /usr/local
COPY app/ ./app/

USER appuser
EXPOSE 8000
CMD ["python", "-m", "app.server"]