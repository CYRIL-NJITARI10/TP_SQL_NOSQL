FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./scripts /app
COPY ./data /app/data


RUN chmod +x /app/run_scripts.sh

CMD ["/app/run_scripts.sh"]