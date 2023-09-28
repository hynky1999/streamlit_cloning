FROM --platform=$TARGETPLATFORM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    docker \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Copy the app
COPY . /app/

EXPOSE 14000-14100
EXPOSE 80


# Run the app
CMD ["gunicorn", "--access-logfile", "-", "--error-logfile", "-", "app:app", "--bind", "0.0.0.0:80"]
