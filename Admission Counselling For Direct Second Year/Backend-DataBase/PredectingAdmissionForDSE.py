'''
    Predecting the Admission for Direct Second Year
'''

import pandas as pd
import mysql.connector as sql
from matplotlib import pyplot as plt

db_connection = sql.connect(host='localhost', database='diploma', user='Atharva', password='Atharva@007')
db_cursor = db_connection.cursor()

db_cursor.execute('SELECT * FROM allocated2018')
table_rows = db_cursor.fetchall()
allocated = pd.DataFrame(table_rows)

db_cursor.execute('SELECT * FROM college2018')
table_rows = db_cursor.fetchall()
college = pd.DataFrame(table_rows)

db_cursor.execute('SELECT * FROM diploma2018')
table_rows = db_cursor.fetchall()
diploma = pd.DataFrame(table_rows)


# Taking Input
gender = input("Enter your gender: ")
category = input("Enter your Category: ")
dper = float(input("Enter your Diploma Per: "))
tenper = float(input("Enter your 10th Per: "))
branch = input("Enter Branch wants: ")
seattype = input("Enter seat type: ")








