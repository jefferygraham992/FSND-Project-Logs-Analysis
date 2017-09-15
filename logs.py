#!/usr/bin/env python
#
# logs.py
#

import psycopg2
from datetime import datetime


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def countArticles():
    """Returns the most popular three articles of all time."""
    db = connect()
    cursor = db.cursor()
    query = ("SELECT articles.title, count(articles.title) FROM log JOIN\n"
             " articles ON log.path ILIKE '%' || articles.slug GROUP BY\n"
             " articles.title ORDER BY count DESC LIMIT 3;")
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print("\"%s\" - %s views") % (result[0], result[1])
    db.close()


def countAuthors():
    """Returns the most popular article authors of all time."""
    db = connect()
    cursor = db.cursor()
    query = ("SELECT authors.name, count(authors.name) FROM log JOIN\n"
             " articles ON log.path ILIKE '%' || articles.slug JOIN authors\n"
             " ON articles.author = authors.id GROUP BY authors.name\n"
             " ORDER BY count DESC;")
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print("%s - %s views") % (result[0], result[1])
    db.close()


def countErrors():
    """Returns the day(s) where more than 1% of requests led to errors."""
    db = connect()
    cursor = db.cursor()
    query = ("SELECT errors.day, errors.count AS errors,\n"
             " sum_all_events.total AS total,\n"
             " ((errors.count/sum_all_events.total) * 100) AS percent FROM\n"
             " errors JOIN sum_all_events ON errors.day = sum_all_events.day\n"
             " WHERE (errors.count/sum_all_events.total) * 100 > 1;")
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        date_object = datetime.strptime(result[0], '%m/%d/%Y')
        print("%s - %.1f%% errors") % (date_object.strftime('%B %d, %Y'),
                                       float(result[3]))
    db.close()


countArticles()
countAuthors()
countErrors()
