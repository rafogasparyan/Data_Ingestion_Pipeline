# Data Ingestion Pipeline

## Overview
This project sets up a data ingestion pipeline using Docker and PostgreSQL. It includes a Python application for ingesting user metrics into a PostgreSQL database, all orchestrated using Docker Compose.

## Project Structure
- **`Dockerfile`**: Defines the environment for the Python application.
- **`docker-compose.yml`**: Orchestrates the application and PostgreSQL containers.
- **`schema.sql`**: SQL script for database schema creation.
- **`app/`**: Contains the Python application code (`ingest_data.py`) for data ingestion.
- **`requirements.txt`**: Lists Python dependencies.


## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Setup and Running
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   docker-compose up --build


### Accessing the PostgreSQL Database

```markdown
## Accessing the PostgreSQL Database

Once your Docker containers are up and running, you can access the PostgreSQL database using the following details:
- **Host**: `localhost`
- **Port**: `5432`
- **Username**: `user`
- **Password**: `password`
- **Database**: `metrics_db`
```


You can use a PostgreSQL client like [pgAdmin](https://www.pgadmin.org/), [DBeaver](https://dbeaver.io/), or [psql](https://www.postgresql.org/docs/current/app-psql.html) to connect.

To connect via the command line using `psql`, use:
   ```bash
   psql -h localhost -p 5432 -U user -d metrics_db
   ```



### Step 6: Database Schema

   ```markdown
## Database Schema

The `schema.sql` script creates the following tables:
- **`talked_time`**: Records metrics related to the amount of time a user has spoken.
- **`microphone_used`**: Logs whether the microphone was used during a session.
- **`speaker_used`**: Logs whether the speaker was used during a session.
- **`voice_sentiment`**: Records the sentiment of the user's voice along with a confidence score.

Indexes are created on commonly queried fields to optimize performance.
```


## Python Application

The Python application (`ingest_data.py`) handles the following:
- Connects to the PostgreSQL database.
- Simulates data fetching (replace with actual data source).
- Inserts data into the respective tables based on the type of metric.


## Important Notes

Before running the setup, please make sure to:

- Replace `<repository-url>` with the URL of your Git repository.
- Replace `<repository-directory>` with the name of your repository directory.
- Verify the `DATABASE_URL` environment variable in the Docker Compose file if you use different database credentials.
- Update the path `/path/to/your/sql/script.sql` with the actual path to your SQL script when applying database changes.
- Check and adjust Docker and Docker Compose configurations if necessary, especially for ports and volume mappings.

These changes are necessary to ensure the setup runs smoothly in your environment.
