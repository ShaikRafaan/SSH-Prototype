
FROM python:3.11-slim

#Set the environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app"

#Working Directory set to /app
WORKDIR /app

#Install the dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

#Copy the dependedncies and install them
COPY server/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt

#Copy the code
COPY . /app/

#Port the container listens to
EXPOSE 8000

#Command to run FastAPI using uvicorn
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
