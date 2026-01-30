import mysql.connector as db


connection = db.connect(host = 'localhost',user = 'admin',
password = 'xqcdd123',database='exams')

if connection.is_connected():
    print("Success of connection")

else:
    print("Connection failed")

cursor = connection.cursor()

query = """CREATE TABLE IF NOT EXISTS EXAM(EXAM_ID INT AUTO_INCREMENT PRIMARY KEY,
   NAME_OF_EXAM VARCHAR(100) , TYPE VARCHAR(50), DATE_OF_EXAM DATE);"""

cursor.execute(query)
connection.commit()


def add_exam(name,typee,date):
    if len(name)==0:
        print("Enter a name")
        return 1

    if len(date)<10:
        print("Enter a  valid date")
        return 1

    if len(typee)==0:
        print("Enter a type of exam")
        return 1

    if int(date[8:10])>31:
        print("Invalid no of days")
        return 1

    if int(date[5:7])>12 or int(date[5:7])<0:
        print("Invalid month")
        return 1

    try:
        query = """INSERT INTO EXAM(NAME_OF_EXAM,TYPE,DATE_OF_EXAM)
        VALUES(%s,%s,%s);"""
        val = (name,typee,date)

        cursor.execute(query,val)
        connection.commit()
        print(f"Record inserted successfully. ID: {cursor.lastrowid}")

    except mysql.connector.Error as err:
        print(f"Failed in adding record: {err}")
        connection.rollback()

    except Exception as e:
        print(f"Unknown Error: {e}")

    
        #print("Error occured")
    return 0


add_exam("NEET","MCQ","2026-01-21")
#add_exam("","","")




