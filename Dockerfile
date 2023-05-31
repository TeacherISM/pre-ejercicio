# Use an appropriate Python base image
FROM public.ecr.aws/lambda/python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY app.py /app/
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run your app
CMD [ "python3", "your_app.py" ]