FROM python:3.11-slim

# prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set working directory inside container
WORKDIR /app

# copy requirements first (Docker caches this layer if unchanged)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of app code
COPY . .

# Flask listens on port 5000
EXPOSE 5000

# run app when the container starts
CMD ["python", "wsgi.py"]