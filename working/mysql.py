import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="kowndi@6772")
print(mydb)
