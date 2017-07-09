#!/usr/bin/env python3
#
# A reporting tool for the news database

from newsdb import (get_most_popular_articles,
                    get_most_popular_authors, get_most_logged_errors)


def main():
    articles = get_most_popular_articles()
    authors = get_most_popular_authors()
    log = get_most_logged_errors()
    print("\n\tMOST POPULAR ARTICLES:\n ")
    for index, (title, views) in enumerate(articles):
        print("""\t\t{}. {}:\n
                \tThis article has been viewed {} times till date.\n"""
              .format(index + 1, title, views))

    print("\n\tMOST POPULAR AUTHORS:\n")
    for index, (name, views) in enumerate(authors):
        print("""\t\t{}. {}:\n
                \tThe author has a total of {} views on his articles.\n"""
              .format(index + 1, name, views))

    print("\n\tMOST LOGGED ERRORS (error > 1%):\n")
    print("\tThe most logged errors were recorded as:\n ")
    for index, (day, error) in enumerate(log):
        print("\t\t{} ---- {}%\n".format(day, error))


if __name__ == "__main__":
    main()
