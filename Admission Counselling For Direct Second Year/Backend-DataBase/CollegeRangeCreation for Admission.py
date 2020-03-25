'''
    Calculating and Storing Database for each college minimum percentage to take admission
'''
import mysql.connector

cr = [[ 'CollegeName' , 'Branch','Gender','Category','Seattype','MinPer']]

try:
    # Connecting to Database
    connection = mysql.connector.connect(host='localhost', database='Diploma', user='Atharva',
                                         password='Atharva@007')
    cursor = connection.cursor()
    
    cursor.execute(" Select CollegeName,Gender,Category,Seattype,min(Marks) from allocated2018 group by collegename,SEATTYPE ")

    result = cursor.fetchall();
    

    for i in result:
        cursor.execute(""" INSERT INTO collegerange2018 VALUES (%s,"Computer",%s,%s,%s,%s)""",(i[0], i[1], i[2], i[3], i[4]))

    connection.commit()
    
except mysql.connector.Error as error:
    connection.rollback()  # rollback if any exception occured
    print("Failed inserting record into collegerange2018 table {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        # print("MySQL connection is closed")
