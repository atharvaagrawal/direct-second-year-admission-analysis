'''
    Storing the Data of Diploma Final Year Merit List 
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
    count = 1

    try:
        # Connecting to Database
        connection = mysql.connector.connect(host='localhost', database='Diploma', user='Atharva',
                                             password='Atharva@007')
        cursor = connection.cursor()

        count = 1
        g = 1
        for i in range(1,173):
            for j in range(4):
                path = "Y:\\Direct Second Year\\Analysis\\Rec\\"+ str(count) +"-page-" + str(g) + "-table-1.csv"
                g = g + 1
                file = open(path, newline='')
                reader = csv.reader(file)

                header = next(reader)  # the first line is the header

                data = []

                for row in reader:
                    MG = int(row[9])
                    SubGrop = int(row[11])

                    if (SubGrop == 301): # For Computer Branch Only 
                        SLGMN = int(row[0])
                        APPID = row[1]
                        Name = row[2]
                        Gender = row[3]
                        DiplomaPer = float(row[4])
                        SSC = float(row[5])
                        SSCM = float(row[6])
                        SSCS = float(row[7])
                        SSCE = float(row[8])
                        CATEGORY = row[13]

                        data.append([SLGMN, APPID, Name, Gender, DiplomaPer, SSC, SSCM, SSCS, SSCE, CATEGORY])
                print(data)
                file.close();

                if len(data) != 0:

                    # Loop to store data
                    for i in data:
                        cursor.execute(
                            """ INSERT INTO Diploma2018 (SLGMN , APPID , NAME , GENDER ,DIPLOMAMARKS ,SSC,SCCMATH ,SSCSCIENCE ,SSCENGLISH ,CATEGORY) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                            (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
                    connection.commit()
                    # print("Record inserted successfully into Diploma2018 table")

                print(count)
            count += 1

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into Diploma2018 table {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")


executeStore()

