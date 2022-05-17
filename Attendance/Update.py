import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Jeralph\Downloads\Database2.accdb')
    print("Connected to a Database")

    Fullname = "Jeralph O. Red"
    Assignment = 90
    Laboratory = 92
    Quiz = 97
    Exam = 99
    user_id = 10

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Fullname = ?, Assignment = ?, Laboratory = ?, Quiz = ?, Exam = ? WHERE id = ?', (Fullname, Assignment, Laboratory, Quiz, Exam, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")