# Use the official Python image from the Docker Hub with Python 3.12.3
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the FastAPI code into the container
COPY . .

# Expose port 80 to the outside world
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
