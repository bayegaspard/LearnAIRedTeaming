# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Install Ollama
RUN pip install llama-cpp-python

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app/app.py"]
