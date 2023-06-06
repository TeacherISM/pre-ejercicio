# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory (i.e. the Flask app) to the container as /app
ADD . /app

# If you don't have a requirements.txt, you can just install Flask directly
RUN pip install --no-cache-dir flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["flask", "run"]