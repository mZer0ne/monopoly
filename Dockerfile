# Use the official Python base image
# FROM python:3.7
FROM python:2.7

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./app .