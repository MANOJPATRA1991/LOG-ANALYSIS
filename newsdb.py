# "Database code" for the DB news.

import psycopg2

DBNAME = "news"


def run_query(query):
    """Excute a query and return the result"""
    try:
        # connect returns a Connection object or raises an exception.
        db = psycopg2.connect(database=DBNAME)
        # makes a Cursor object from the connection.
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if c is not None:
            db.close()


def get_most_popular_articles():
    """Return three most popular articles of all time, most popular first"""
    data = run_query("select title, views from articleShortInfo limit 3")
    return data


def get_most_popular_authors():
    """Return popular authors, most popular first"""
    data = run_query("""select name, sum(views) as views
                       from articleShortInfo
                       group by name
                       order by views desc""")
    return data


def get_most_logged_errors():
    """Return day with logged errors greater than 1%"""
    data = run_query("""select  to_char(a.time, 'Dy, Mon DD, YYYY') as day,
                        round(a.errors*100/b.total::numeric, 2) as error
                        from ErrorRequests as a, LogRequests as b
                        where (a.errors > 0.01*b.total) and (a.time = b.time)
                        order by error desc""")
    return data
