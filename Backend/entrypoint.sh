#!/bin/sh

# Wait for PostgreSQL to be ready
echo "Waiting for database..."
while ! nc -z db 5432; do   
  sleep 1
done
echo "Database is ready."

# Run migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the server
echo "Starting server..."
exec "$@"