TRUNCATE TABLE current_weather;
insert into current_weather (
    id, country, city, date, temperature, sunrise, sunset, wind_speed, sea_level, weather_description
)
select 
	id, 
	country , 
	name as city, 
	datetime::date as date, 
	ROUND((temperature - 273.15)::numeric ,1) as temperature, 
	sunrise::time AS sunrise, 
	sunset::time AS sunset, 
	wind_speed, 
	sea_level, 
	weather_description 
from weather 
where batch_id = (select batch_id from weather order by datetime desc limit 1) 




