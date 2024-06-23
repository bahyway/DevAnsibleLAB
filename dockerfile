# Use the official PostgreSQL image from the Docker Hub
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER bfadam
ENV POSTGRES_PASSWORD bF@d@m22011964
ENV POSTGRES_DB bfOffice01

# Expose the PostgreSQL port
EXPOSE 5432

# Copy initialization script
COPY init.sql /docker-entrypoint-initdb.d/


