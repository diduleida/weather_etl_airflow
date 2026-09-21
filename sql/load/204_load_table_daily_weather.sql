insert into daily_weather (country,city,date,avg_temperature_day,max_temperature_day,min_temperature_day)
select cw.country,
	cw.city,
	cw.date,
	avg(cw.temperature) as avg_temperature_day,
	max(cw.temperature) as max_temperature_day,
	min(cw.temperature) as min_temperature_day
from current_weather cw 
WHERE cw.date = CURRENT_DATE - INTERVAL '1 day'
group by 1,2,3


