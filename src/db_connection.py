import mysql.connector 

def get_connection():
   connection =  mysql.connector.connect(
    host="localhost",
        user="root",
        password="pooja",
        database="student_pipeline"
   )
   return connection