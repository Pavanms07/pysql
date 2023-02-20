

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pavanms@1234"
    )   
try:
     
    mycursor = mydb.cursor()
    
finally:

    print("DB COnnected")
    
    mycursor.execute("select * from  scrap_task.employee1 limit 3 ")
    for x in mycursor:
          print(x)

