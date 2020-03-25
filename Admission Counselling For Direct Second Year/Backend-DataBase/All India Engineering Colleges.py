'''
    All India Colleges WebScrapping
'''
import requests
import bs4
import mysql.connector
res = requests.get("https://www.nirfindia.org/2019/EngineeringRankingALL.html", verify=False)

#print(res.text)

soup = bs4.BeautifulSoup(res.text,'lxml');

print(soup)


tabledata = soup.select('td')


seats = []
count = 0

s = ['','','']
r = 0
b = 0

for i in tabledata:
    count+=1
    b +=1

    if(count<=3):
        s[r] = i.getText()
        r += 1

    if (count == 3):
        count = 0

    if(r == 3):
        seats.append(s)
        s = ['','','']
        r=0

print(seats)

try:
    # Connecting to Database
    connection = mysql.connector.connect(host='localhost', database='Diploma', user='Atharva',
                                         password='Atharva@007')
    cursor = connection.cursor()

    for i in seats:
        cursor.execute(""" INSERT INTO ALLINDIACOLLEGE2018 VALUES (%s,%s,%s)""",(i[0], i[1], i[2]))

    connection.commit()

except mysql.connector.Error as error:
    connection.rollback()  # rollback if any exception occured
    print("Failed inserting record into ALLINDIACOLLEGE2018 table {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        # print("MySQL connection is closed")
