CREATE TABLE if not EXISTS daily_weather(
    country VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    date DATE NOT NULL,
    avg_temperature_day FLOAT,
    max_temperature_day FLOAT,
    min_temperature_day FLOAT,

    PRIMARY KEY (date, city)
)