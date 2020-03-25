# All Diploma Institute in Maharashtra Course Wise

import requests
import bs4
import mysql.connector

rows = 0
try:
    # Getting Complete Website Response and Code in web_code
    web_code = requests.get("https://dse19.mahacet.org.in/dse19/index.php/hp_controller/instcourses", verify=False)

    # Creating Beautiful Object
    soup = bs4.BeautifulSoup(web_code.text, 'lxml')

    # Taking Table Data
    table_td = soup.select('td')

    # Creting 2D List
    #['SRNO','CHOICE CODE','COLLEGE NAME','COURSE NAME','COURSE TYPE','SI']
    rows = []
    count = 0

    # Storing Respective table data into respective column of List
    single_row = ['','','','','','']
    coll = 0
    for i in table_td:
        count += 1
        if count >= 4:
            single_row[coll] = i.getText()
            coll += 1

        if coll == 5:
            rows.append(single_row)
            single_row = ['','','', '', '', '']
            coll = 0

    # Getting College Name
    college_name = []
    count = 0
    for i in soup.select('th'):
        count+=1
        # Greater than 6 due to first 5 are Headings
        if(count>=6):
            college_name.append(i.getText())

    c = 0
    row_index = 0

    # Adding College Names
    for i in rows:
        if( row_index != 1 and rows[row_index][0] == '1' ):
            c +=1

        rows[row_index][5] += college_name[c]
        #print(c, row_index, rows[row_index])

        row_index += 1

        if row_index == 1800:
            break

    for i in rows:
        print(i)
            

    # Changing Type of Variable from String to respective type
    count=0
    for i in rows:
        rows[count][0] = int(i[0])
        rows[count][1] = i[1].replace('F','')
        rows[count][1] = int(i[1])
        rows[count][4] = int(i[4])

except:
    print("Error")

'''
try:
    # Connecting to Database
    connection = mysql.connector.connect(host='localhost', database='Diploma', user='Atharva',
                                         password='Atharva@007')
    cursor = connection.cursor()
    count=0
    for i in rows:
        if (count !=0):
            cursor.execute(
                """ INSERT INTO college2018 VALUES (%s,%s,%s,%s,%s,%s)""",(i[0], i[1], i[2], i[3], i[4], i[5]))
        count+=1
    connection.commit()

except mysql.connector.Error as error:
    connection.rollback()  # rollback if any exception occured
    print("Failed inserting record into Diploma2018 table {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        # print("MySQL connection is closed")
'''
