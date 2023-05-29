# Use an official Python runtime as a parent image
FROM python:3.7-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy only requirement file in order to optmizize build process
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Define environment variable
ENV NAME World_PPM_2023_ok

# Run app.py when the container launches
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]