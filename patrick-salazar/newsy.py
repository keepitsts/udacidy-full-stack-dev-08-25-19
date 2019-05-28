
import psycopg2


DBNAME = "news"


def get_questionOne():
    print('\n----------------------------------------------------------------')
    print("\nPlease see below for the top 3 articles -by number of views- and the number of views each article had. \n")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # create view tops as select replace(path, '/article/', '') as slugpath, count(*) as views from log group by slugpath order by views;
    c.execute("select articles.title, tops.views from articles join tops on tops.slugpath = articles.slug order by views desc limit 3 offset 1;")
    answer = c.fetchall()
    for title, views in answer:
        print('Article: ' + str(title) + ' ' + '   Number of Views:' + ' ' + str(views) + '\n')
    db.close()


get_questionOne()


def get_questionTwo():
    print('\n----------------------------------------------------------------')
    print("\nPlease see below for the top authors -by number of views- and the number of views each author had. \n")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # create view authnameslug as select authors.name, articles.slug from authors join articles on authors.id = articles.author group by authors.name, articles.slug order by authors.name;
    c.execute("select authnameslug.name as author, sum(tops.views) as views from authnameslug join tops on authnameslug.slug = tops.slugpath group by authnameslug.name order by views desc;")
    answer = c.fetchall()
    for author, views in answer:
        print('Author: ' + str(author) + ' ' + '   Number of Views:' + ' ' + str(views) + '\n')
    db.close()


get_questionTwo()


def get_questionThree():
    print('\n----------------------------------------------------------------')
    print("\nPlease see below for all dates when errors were greater than 1 percent of all responses. \n")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # create view allstatus as select date(time) as date, count(status) as total from log group by date order by date;
    # create view errors as select date(time) as date, count(status) as err_responses from log where status != '200 OK' group by date order by date;
    # create view finalp as select date, err_responses, responses, round(err_responses * 100.0 / responses, 1) as percent from percent;
    c.execute("select date, percent from finalp where percent > 1.0;")
    answer = c.fetchall()
    for date, percent in answer:
        print('On ' + str(date) + ', ' + 'The percentage of total status responses that were error messages was ' + str(percent) + '%.\n')
    db.close()


get_questionThree()
