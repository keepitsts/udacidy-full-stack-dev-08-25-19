#!/usr/bin/env python3

import psycopg2

dbname = "news"


def top_three_articles():
    db = psycopg2.connect(database=dbname)
    c = db.cursor() 
    """  
    top_articles =c.execute("select path,count(path) as hits from log 
    group by path")
    """
    top_articles = c.execute("select slug, count slug as pageviews from \
    articles left join log on replace(log.path, '/article/', ') = \
    articles.slug group by slug")
    db.close()
    return top_articles


def top_author() 
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    """  
    top_articles =c.execute("select path,count(path) as hits from log group by path")
    """ 
    top_author = c.execute("select slug, count slug as pageviews from articles\
    left join log on replace(log.path, '/article/', ') = articles.slug group\
    by slug")
    db.close()
    return top_author

def errors()
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    error_percentage = c.execute('select time, status, count(status) as num_errors\
    group by time order by num_errors ')
    db.close()
    return errors