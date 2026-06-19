FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install flask requests

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python -c "import requests; requests.get('http://localhost:5000/health')"

CMD ["python", "src/app.py"]