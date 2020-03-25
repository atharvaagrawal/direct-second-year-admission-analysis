'''
    Storing data for Student Placed in Top Colleges of Maharashta 
'''
import csv
import mysql.connector
import os.path
import pandas as pd
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

def executeStore():
    print("Hello")
    if not os.path.exists('govtamravati2018.csv'):
        print("First Download the file")
        exit(0)

    path = "govtamravati2018.csv"
    file = open(path, newline='')
    reader = csv.reader(file)

    COLLEGENAME = "Government College Of Engineering Amravati"

    header = next(reader)  # the first line is the header

    data = []
    count = 1


    
    for row in reader:
        MERITNO = int(row[1])
        MARKS  = float(row[3].replace('%', ''))
        APPID = row[4]
        NAME = row[5]
        GENDER = row[6]
        CATEGORY = row[7]
        SEATTYPE = row[9]
        
        data.append([COLLEGENAME , MERITNO , MARKS , APPID ,NAME ,GENDER,CATEGORY ,SEATTYPE])
        count+=1;

    # DataBase Connection
    try:
        connection = mysql.connector.connect(host='localhost', database='Diploma', user='Atharva', password='Atharva@007')
        cursor = connection.cursor()
        # Loop to store data
        for i in data:
            cursor.execute(""" INSERT INTO ALLOCATED2018 (COLLEGENAME , MERITNO , MARKS , APPID ,NAME ,GENDER,CATEGORY ,SEATTYPE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                           (i[0], i[1], i[2], i[3], i[4],i[5], i[6], i[7]))
        connection.commit()
        print("Record inserted successfully into ALLOCATED2018 table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into Diploma2018 table {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            file.close()
            print("MySQL connection is closed")

executeStore()
