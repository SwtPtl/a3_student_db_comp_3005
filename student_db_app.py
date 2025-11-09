import psycopg2

DB_NAME = 'assignment_4_db' #your db name
USER = 'postgres' #your username
PASSWORD = '12345' #your password
HOST = 'localhost' #your host

# Connect and return connection/cursor
def connect():
    conn = psycopg2.connect(database=DB_NAME, user=USER, password=PASSWORD, host=HOST)
    return conn, conn.cursor()

# function to get info of all students
def getAllStudents():
    conn, cur = connect()
    cur.execute('SELECT * FROM students;')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

# function to add student info
def addStudent():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    email = input('Email: ')
    date = input('Enrollment date (YYYY-MM-DD): ')
    conn, cur = connect()
    cur.execute('''
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s)
    ''', (first_name, last_name, email, date))
    conn.commit()
    print('Added student.')
    getAllStudents()
    conn.close()

# function to update email
def updateStudentEmail():
    sid = input('Student ID to update: ')
    new_email = input('New email: ')
    conn, cur = connect()
    cur.execute('UPDATE students SET email = %s WHERE student_id = %s;', (new_email, sid))
    conn.commit()
    print('Updated student email.')
    getAllStudents()
    conn.close()

# function to delete a student
def deleteStudent():
    sid = input('Student ID to delete: ')
    conn, cur = connect()
    cur.execute('DELETE FROM students WHERE student_id = %s;', (sid,))
    conn.commit()
    print('Deleted student.')
    getAllStudents()
    conn.close()

#main menu function
def menu():
    while True:
        print('\nOptions:')
        print('1. List all students')
        print('2. Add a student')
        print('3. Update student email')
        print('4. Delete student')
        print('5. Exit')
        choice = input('Select an option: ')
        if choice == '1':
            getAllStudents()
        elif choice == '2':
            addStudent()
        elif choice == '3':
            updateStudentEmail()
        elif choice == '4':
            deleteStudent()
        elif choice == '5':
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    menu()
