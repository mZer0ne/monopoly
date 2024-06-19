# Use the official Python base image
FROM python:2.7

# Install dependencies
RUN apt-get clean && rm -r /var/lib/apt/lists/* && apt-get update --fix-missing
RUN apt-get install -y --no-install-recommends gettext libgettextpo-dev

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
ADD entrypoint.sh /entrypoint.sh
COPY ./app .

# Set chmod
RUN chmod +x /entrypoint.sh

# Clean cache
RUN apt-get clean && rm -r /var/lib/apt/lists/*


# Enrtypoint
ENTRYPOINT ["/entrypoint.sh"]