# Use Python base image
FROM python:3.10-slim

# Create app directory inside container
WORKDIR /app

# Copy Python script into container
COPY create_dirs.py /app/create_dirs.py

# Run script when container starts
CMD ["python", "create_dirs.py"]