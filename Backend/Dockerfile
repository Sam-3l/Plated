# Using official Python runtime as a parent image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies separately to improve caching
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the rest of the project files
COPY . .  

# Give execution permission to the entrypoint script
RUN chmod +x /app/entrypoint.sh  

# Set the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]

# Expose the application port
EXPOSE 8000

# Default command to start Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
