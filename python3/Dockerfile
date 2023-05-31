FROM python:3.11

# Set working directory
WORKDIR /app

# Copy the necessary files
COPY requirements.txt .
COPY execute.sh .
COPY src/ ./src/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Set execute.sh as the entrypoint
ENTRYPOINT ["/app/execute.sh"]
    