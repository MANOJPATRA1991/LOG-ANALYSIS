# "Database code" for the DB news.

import psycopg2

DBNAME = "news"


def get_most_popular_articles():
    """Return three most popular articles of all time, most popular first"""
    # connect returns a Connection object or raises an exception.
    conn = psycopg2.connect(database=DBNAME)
    # makes a Cursor object from the connection.
    cursor = conn.cursor()
    cursor.execute("select title, views from articleShortInfo limit 3")
    data = cursor.fetchall()
    conn.close()
    return data


def get_most_popular_authors():
    """Return popular authors, most popular first"""
    # connect returns a Connection object or raises an exception.
    conn = psycopg2.connect(database=DBNAME)
    # makes a Cursor object from the connection.
    cursor = conn.cursor()
    cursor.execute("""select name, sum(views) as views
                   from articleShortInfo
                   group by name
                   order by views desc""")
    data = cursor.fetchall()
    conn.close()
    return data


def get_most_logged_errors():
    """Return day with logged errors greater than 1%"""
    # connect returns a Connection object or raises an exception.
    conn = psycopg2.connect(database=DBNAME)
    # makes a Cursor object from the connection.
    cursor = conn.cursor()
    cursor.execute("""select  to_char(a.time, 'Dy, Mon DD, YYYY') as day,
                    round(a.errors*100/b.total::numeric, 2) as error
                    from ErrorRequests as a, LogRequests as b
                    where (a.errors > 0.01*b.total) and (a.time = b.time)""")
    data = cursor.fetchall()
    conn.close()
    return data
