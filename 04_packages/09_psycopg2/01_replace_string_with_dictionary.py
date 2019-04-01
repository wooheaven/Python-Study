import psycopg2
from psycopg2.extensions import AsIs

#Create your connection and cursor...

cursor.execute(
    "SELECT * FROM %(table)s", 
    {"table": AsIs("my_awesome_table")}
)

