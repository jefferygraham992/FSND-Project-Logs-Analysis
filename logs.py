#!/usr/bin/env python
#
# logs.py
#

import psycopg2
from datetime import datetime

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")

# What are the most popular three articles of all time?
# Who are the most popular article authors of all time?
# On which days did more than 1% of requests lead to errors?



def countArticles():
    """Returns the most popular three articles of all time."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT articles.title, count(articles.title) FROM log JOIN"
    + " articles ON log.path ILIKE '%' || articles.slug GROUP BY articles.title "
    + "ORDER BY count DESC LIMIT 3;")
    results = cursor.fetchall()
    for result in results:
        print("%s - %s views") % (result[0], result[1])
    db.close()


def countAuthors():
    """Returns the most popular article authors of all time."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT authors.name, count(authors.name) FROM log JOIN "
    + "articles ON log.path ILIKE '%' || articles.slug JOIN authors ON "
    + "articles.author = authors.id GROUP BY authors.name ORDER BY count DESC;")
    results = cursor.fetchall()
    for result in results:
        print("%s - %s views") % (result[0], result[1])
    db.close()


def countErrors():
    """Returns the day(s) where more than 1% of requests led to errors."""
    db = connect()
    cursor = db.cursor()
    # cursor.execute("CREATE VIEW errors AS SELECT status, to_char(time, 'mm/dd/yyyy') AS DAY, COUNT(STATUS) FROM log GROUP BY DAY, status HAVING status = '404 NOT FOUND';")
    # cursor.execute("CREATE VIEW all_events AS SELECT status, to_char(time, 'mm/dd/yyyy') AS DAY, COUNT(STATUS) FROM log GROUP BY DAY, status;")
    # cursor.execute("CREATE VIEW total_events AS SELECT day, SUM (count) as total FROM all_events GROUP BY day;")
    cursor.execute("SELECT errors.day, errors.count AS errors, sum_all_events.total AS total, ((errors.count/sum_all_events.total) * 100) AS percent FROM errors JOIN sum_all_events ON errors.day = sum_all_events.day WHERE (errors.count/sum_all_events.total) * 100 > 1;")
    results = cursor.fetchall()
    for result in results:
        date_object = datetime.strptime(result[0], '%m/%d/%Y')
        print("%s - %.1f%% errors") % (date_object.strftime('%B %d, %Y'), float(result[3]))
    db.close()


# countArticles()
# countAuthors()
countErrors()
