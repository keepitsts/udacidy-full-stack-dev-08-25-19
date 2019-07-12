import psycopg2

dbname = "news"

db = psycopg2.connect("dbname=news")

def top_three_articles():   
    c = db.cursor()   
    #top_articles =c.execute("select path,count(path) as hits from log group by path") 
    top_articles = c.execute("select slug, count slug as pageviews from articles \
    left join log on replace(log.path, '/article/', ') = articles.slug group by slug") 
    return top_articles


def top_author() 
c = db.cursor()   
    #top_articles =c.execute("select path,count(path) as hits from log group by path") 
    top_author = c.execute("select slug, count slug as pageviews from articles \
    left join log on replace(log.path, '/article/', ') = articles.slug group by slug") 
    return top_author

def errors()
    db.cursor()
    error_percentage = c.execute('select time, status, count(status) as num_errors group\
     by time order by num_errors ')