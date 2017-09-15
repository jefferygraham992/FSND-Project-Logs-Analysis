# FSND-Project-Logs-Analysis
# cursor.execute("CREATE VIEW errors AS SELECT status, to_char(time, 'mm/dd/yyyy') AS DAY, COUNT(STATUS) FROM log GROUP BY DAY, status HAVING status = '404 NOT FOUND';")

cursor.execute("CREATE VIEW all_events AS SELECT status, to_char(time, 'mm/dd/yyyy') AS DAY, COUNT(STATUS) FROM log GROUP BY DAY, status;")

cursor.execute("CREATE VIEW total_events AS SELECT day, SUM (count) as total FROM all_events GROUP BY day;")
