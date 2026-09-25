# syntax=docker/dockerfile:1

FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    tini \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    --extra-index-url https://pypi.org/simple \
    -r requirements.txt

COPY . .

ENV HF_HOME=/app/.cache/huggingface
ENV HF_HUB_OFFLINE=1

RUN python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='intfloat/multilingual-e5-small', allow_patterns=['*.json', '*.txt', 'sentencepiece.bpe.model', 'model.safetensors', '1_Pooling/*'], ignore_patterns=['*.bin', 'onnx/*', 'openvino/*', '*.h5', '*.msgpack'])"

RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=5s --start-period=60s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/healthz')" || exit 1

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["uvicorn", "engine:app", "--host", "0.0.0.0", "--port", "8000"]