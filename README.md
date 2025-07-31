# ========== README.md ==========
# CMS Medicare Data Pipeline
This project provides a fully containerized data engineering pipeline that ingests, cleans, and transforms the CMS Medicare Inpatient Hospitals - by Geography and Service dataset (https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-geography-and-service) and creates an app that identifies the 10 cheapest cities and states for each DRG. The pipeline uses  It includes:

Airflow – Orchestrates the ETL pipeline
PostgreSQL – Stores raw and processed data
dbt – Creates analytical model
Streamlit – Provides a UI for interactive cost exploration

# Features
Automatic download of CMS inpatient hospital data

Cleans and loads data into PostgreSQL

dbt models for cost aggregation

Streamlit app to visualize and explore costs

Fully containerized with Docker Compose

# Prerequisites
Docker and Docker Compose installed


# Project Structure
cms-data-pipeline/

├── dags/                     # Airflow DAGs

│   └── cms_etl_dag.py

├── data/                     # Populated by the DAG

│   └── raw_data.csv

├── dbt/                      # dbt models and config

│   ├── models/

│   │   ├── cost_by_city_and_state.sql

│   │   └── distinct_drgs.sql

│   └── dbt_project.yml

│   └── profiles.yml

├── scripts/                  # ETL scripts

│   └── cms_etl.py

├── streamlit/                # Streamlit visualization app

│   └── app.py

├── docker-compose.yml

├── dockerfile.airflow

├── dockerfile.streamlit

└── README.md


# Setup Instructions
Clone the repository:
git clone https://github.com/codydance/CMS-Data-Explorer.git
cd CMS-Data-Explorer

Start all services:
docker-compose up --build

Airflow UI: http://localhost:8080 (username: admin , password: admin)
Streamlit app: http://localhost:8501

# Running the Pipeline
The pipeline is automatically triggered with "docker-compose up --build". Further runs can be triggered from the Airflow UI. 

# Check PostgreSQL Database:
docker-compose exec postgres psql -U cms_user -d cms_db

Example Queries:

    \dt (list tables)

    SELECT * FROM cms_data LIMIT 10;

# Development Notes
Volumes: A 'pgdata' Docker volume is used for PostgreSQL persistence.

Environment Variables: Database credentials are set in docker-compose.yml.

Custom Dependencies: Installed via Dockerfile.airflow using requirements.txt.

# Resetting the project:
docker-compose down -v
docker-compose up --build
s

