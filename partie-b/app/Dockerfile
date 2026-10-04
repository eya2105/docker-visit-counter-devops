# Alpine base: ~50 MB instead of ~1 GB for the full Python image
FROM python:3.12-alpine

WORKDIR /app

# Dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Non-root user for security
RUN adduser -D appuser

# Code 
COPY app.py .
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]