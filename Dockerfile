FROM python:3.11-alpine

# Set working directory
WORKDIR /opt/opencti-connector-misp-feed

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN apk add --no-cache \
    git \
    build-base \
    libffi-dev \
    libmagic \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del git build-base \
    && rm -rf /var/cache/apk/*

# Copy source code
COPY src/ ./

# Set entrypoint
ENTRYPOINT ["python", "main.py"]
