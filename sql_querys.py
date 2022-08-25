# INFO
# Вывести топ 5 самых коротких по длительности перелетов.  Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
# SELECT flight_no, min(scheduled_arrival-scheduled_departure) AS duration FROM flights GROUP BY flight_no ORDER BY duration LIMIT 5;
TASK_1_QUERY = """
SELECT flight_no, (scheduled_arrival-scheduled_departure) AS duration FROM flights ORDER BY duration LIMIT 5;
"""
#  flight_no | duration
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# INFO
# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
SELECT flight_no, COUNT(1) FROM flights GROUP BY flight_no HAVING COUNT(1)<50 ORDER BY COUNT(1) DESC LIMIT 3;
"""
#  flight_no | count
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# INFO
# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """
SELECT COUNT(CASE WHEN dep = arr THEN 1 ELSE NULL END) from 
(SELECT flight_id, ad.timezone AS dep, a_d.timezone AS arr FROM flights AS f 
INNER JOIN airports_data AS ad ON f.departure_airport = ad.airport_code 
INNER JOIN airports_data AS a_d ON f.arrival_airport = a_d.airport_code) AS sel;
"""
# select count(1) from
# (select flight_id, ad.timezone as dep, a_d.timezone as arr from flights as f
# inner join airports_data as ad on f.departure_airport = ad.airport_code
# inner join airports_data as a_d on f.arrival_airport = a_d.airport_code)
# as sel where sel.dep = sel.arr;

#  count
# --------
#  16824
