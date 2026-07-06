# Base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r app/requirements.txt
RUN pip install --no-cache-dir -r cleanup/requirements.txt

# Default command
CMD ["python", "app/app.py"]