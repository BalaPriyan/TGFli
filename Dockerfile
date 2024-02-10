# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment and activate it
RUN pip3 install virtualenv
RUN virtualenv venv
RUN /app/venv/bin/activate

# Install dependencies
RUN pip3 install -r /app/requirements.txt

# Set environment variables
ENV DATABASE_URL=<your_database_url>

# Setup Database
RUN psql $DATABASE_URL < /app/scripts/migrate.sh

# Expose the port the app runs on
EXPOSE 8000

# Command to run your application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
