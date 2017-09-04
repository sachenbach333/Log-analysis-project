#!/usr/bin/python -tt

import psycopg2


def connect(database_name="news"):
	try:
	    database_connection = psycopg2.connect("dbname={}".format(database_name))
	    cursor = database_connection.cursor()
	    return database_connection, cursor
	except psycopg2.Error as e:
   	    print "Unable to connect to the database"
	    sys.exit(1)


def get_query(query):
	"""Opens, connects, and closes each databse query"""
	db, cursor = connect()
	cursor.execute(query)
	results = cursor.fetchall()
	db.close()
	return results;


def popular_articles():
	"""Fetches and prints the 3 most popular articles of all time"""
	query = """
		select title, count(title) as views
	  	   from articles, log
		   	where log.path = concat('/article/', articles.slug)
		  	group by title
		   order by views desc
	  	   limit 3
		   """

	results = get_query(query)

	print("Top 3 articles:")
	for i in range(0, len(results), 1):
     	    print " \""+ results[i][0] + "\" - "+ str(results[i][1]) + "views"

def popular_authors():
	"""Fetches and prints the most popular authors"""
	query = """
	   	select authors.name, count(articles.author) as views
                  from articles, authors, log
                       where articles.author = authors.id
                       and log.path = concat('/article/', articles.slug)
                group by authors.name
                order by views desc;
                """

	results = get_query(query)

	print("Most popular authors:")
	for i in range(0, len(results), 1):
		print " \" "+ results[i][0] + "\" - "+ str(results[i][1]) + "views"


def most_error_days():
	"""Creates query and sub-query that finds days with errors, converts to % and returns those with
	    higher than 1%"""
	query = """
		select *
		      from
			  (select date(time),
 				round(100.0*sum(case log.status when '404 NOT FOUND' 
 				then 1 else 0 end)/count(log.status),2) as percentage 
  			 	from log group by date(time) order by percentage desc)
				   as subq
				where percentage >= 1.0;
			   """

	results = get_query(query)

	print("Days with request errors of more than 1%:")
	for i in range(0, len(results), 1):
		print ('\t' + str(results[i][0]) + ' -- ' + str(results[i][1]) + ' %')	

if __name__ == '__main__':
	popular_articles()
	popular_authors()
	most_error_days()
