# Use the official PostgreSQL image as a base
FROM postgres:15

# Set environment variables for database setup
#ENV POSTGRES_DB=otree
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=mypassword

# Optional: copy initialization SQL scripts (executed automatically)
# COPY init.sql /docker-entrypoint-initdb.d/

# Expose PostgreSQL default port
EXPOSE 5432
