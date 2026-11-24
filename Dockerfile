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
CMD ["python", "-c", "from app.filemanager import FileManager; fm = FileManager('/home/appuser/data'); fm.write_file('hello.txt', 'Файловый менеджер работает'); print(fm.list_dir()); print(fm.read_file('hello.txt'))"]