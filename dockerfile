# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the .env file into /app
COPY .env .

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app/main.py"]
