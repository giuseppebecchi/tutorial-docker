# Use the official Python base image
FROM python:3.9-slim

# Set environment variables to:
# 1) prevent Python from writing .pyc files (compiled Python files)
# 2) prevent to buffer the output: makes it easier to see the output of your application in real-time
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
# apt-get clean && rm -rf /var/lib/apt/lists/* commands are used to reduce the image size by cleaning up the package lists.
RUN apt-get update && apt-get install -y \
    build-essential \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /flask-app

# Copy requirements.txt
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY app .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
