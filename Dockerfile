# Use an official Python runtime as the parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages
RUN pip install --upgrade openai 
RUN pip install flask

# Run the command to start the Flask application
CMD ["python", "app.py"]
