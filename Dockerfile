# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app/ /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run ingest_data.py when the container launches
CMD ["python", "ingest_data.py"]
