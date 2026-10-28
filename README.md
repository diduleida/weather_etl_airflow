# Weather ETL Pipline
## Overview

This project implements an ETL pipline that extracts weather data from OpenWeatherMap API, validates, transform and loads data into a PostgresSQL data warehause

Apache Airflow orchestrates the ETL pipeline, automating task execution and scheduling.

Docker Compose is used to run the project services, included PostgresSQL and MinIO, while Python and SQL handle data extraction, validation, transformation and loading

## Architecture
```
OpenWeatherMap API
|
v
Extract (Python)
|
v
MinIO (raw json)
|
v
Validation (Pandas)
|
v
Transform (Pandas)
|
v
Load Raw Weather
|
+ ----> Weather
|
+ ----> Current weather 
|
+ ----> Daily weather
```

## Tech Stack
- Python
- SQL
- Pandas
- PostgresSQL
- Docker / Docker Compose
- MinIO
- Apache Airflow        


## Project Structure
```
|
|- src/ 
    |- config
    |- db
    |- extract
    |- storage
    |- validation
    |- transform
    |- load
|
|- sql/
    |- create/
        |- 101_create_table_weather_raw
        |- 102_create_table_weather
        |- 103_create_table_current_weather
        |- 104_create_table_daily_weather
    |- load/
        |- 202_load_table_weather
        |- 203_load_table_current_weather
        |- 204_load_table_daily_weather
|
|- docker-compose.yml
|- Dockerfile 
|- requirements.txt
|- README.md
```


## Database Schema

weather_raw - stores raw api weather
weather - cleand and typed weather data
current_weather - stores the last weather data for each city
daily_weather - contains average daily data for each city


## ETL pipiline

### Extract 
extract raw data from the API 

### Storage
save raw data to MinIO

## Validation 
validation raw data 
make sure it is not contain isna/duplicate/is empty

## Transform
to type and clean the data to the appropriate data types

## Load
load data weather to db

## db
data base connection


## How to run 
- make sure Docker Desktop is running
- run the following command to start the services at terminal in the project directory:
```bash
docker compose up -d
```
