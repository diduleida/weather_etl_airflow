CREATE TABLE IF NOT EXISTS weather(
    id BIGINT NOT NULL,
    batch_id VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    datetime TIMESTAMPTZ NOT NULL,
    temperature FLOAT,
    feels_like FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    sea_level INT,
    wind_speed FLOAT,
    rain_1h FLOAT,
    cloudiness INT,
    sunrise TIMESTAMPTZ,
    sunset TIMESTAMPTZ,
    weather_description VARCHAR,

    PRIMARY KEY (datetime, id)
)