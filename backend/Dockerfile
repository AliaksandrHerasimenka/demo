FROM python:3.12-slim

WORKDIR /app

EXPOSE 8080

COPY --chown=appuser:appuser app.py .

RUN adduser appuser && \
    chown -R appuser:appuser /app

RUN pip install gunicorn flask

USER appuser

HEALTHCHECK --interval=30s --timeout=2s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
