FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-traditional \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create a script to wait for DB and then start the app
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
until nc -z -v -w30 $MYSQL_HOST 3306; do\n\
  echo "Waiting for database connection..."\n\
  sleep 2\n\
done\n\
\n\
echo "Database is up - starting app"\n\
exec gunicorn app:app --bind 0.0.0.0:3000\n\
' > /app/entrypoint.sh \
&& chmod +x /app/entrypoint.sh

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
ENTRYPOINT ["/app/entrypoint.sh"]