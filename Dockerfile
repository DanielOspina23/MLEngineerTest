# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory
RUN mkdir -p ./MLTest
WORKDIR ./MLTest

#Copy requirment.txt
COPY requirements.txt ./io

# Install any needed packages specified in requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . ./

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run main.py when the container launches
CMD python server.py
