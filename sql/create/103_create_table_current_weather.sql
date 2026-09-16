CREATE TABLE IF NOT EXISTS current_weather (
    id BIGINT NOT NULL,
    country VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    date DATE NOT NULL,
    temperature NUMERIC(5,2),
    sunrise TIME,
    sunset TIME,
    wind_speed FLOAT,
    sea_level FLOAT,
    weather_description VARCHAR,

    PRIMARY KEY (city)
)