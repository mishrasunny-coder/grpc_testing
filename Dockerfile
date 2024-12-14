# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Poetry
RUN pip install poetry

# Install dependencies via Poetry
RUN poetry install --no-dev

# Expose the gRPC server port (e.g., 50051)
EXPOSE 50051

# Command to run the gRPC server
CMD ["poetry", "run", "python", "server.py"]
