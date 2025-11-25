Use a slim Python image for a smaller final image size

FROM python:3.11-slim

Set the working directory in the container

WORKDIR /app

Copy only the dependencies file first to leverage Docker layer caching

COPY requirements.txt .

Install dependencies

Using --no-cache-dir to keep the image slim

RUN pip install --no-cache-dir -r requirements.txt

Copy the rest of the application code

COPY . .

Expose the port the app runs on (gunicorn default is 5000)

EXPOSE 5000

Command to run the application using gunicorn for production stability

The environment variable APP_VERSION is passed in during the CI/CD process

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
