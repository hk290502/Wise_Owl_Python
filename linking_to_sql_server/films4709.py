# the main Python module to link to SQL Server

import pyodbc

# connect to the movies database (this uses Windows

# authentication and assumes your SQL Server instance

# is called sql2019 on your currnet computer)

movies_database_connnection = pyodbc.connect(

r"Driver=SQL Server;"

r"Server=.\sql2019;"

r"Database=Movies_01;"

r"Trusted_Connection=yes;"

)

# create an SQL command to show 100 longest films

sql_query = "SELECT Title, RunTimeMinutes, OscarWins FROM Film ORDER BY RunTimeMinutes DESC"

# create a cursor to get this data

movies_cursor = movies_database_connnection.cursor()

movies_cursor.execute(sql_query)

# for each of these 100 longest films, show ones winning more than 7 Oscars

films = movies_cursor.fetchmany(100)