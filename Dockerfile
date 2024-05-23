# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variable
ENV MY_ENV_VAR="Hello from Docker!"

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]
