# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
RUN apt-get -qq update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app
WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m pip install --upgrade \
    pip \
    wheel


# Install dependencies
RUN pip3 install -r /app/requirements.txt

# Set environment variables
ENV DATABASE_URL=postgres://koyeb-adm:ftqdyolX9Tg0@ep-quiet-resonance-a2yei523.eu-central-1.pg.koyeb.app/koyebdb

# Setup Database
RUN psql $DATABASE_URL < /app/scripts/migrate.sh

# Expose the port the app runs on
EXPOSE 8000

# Command to run your application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
