# Student Database Application - COMP 3005 Assignment 3

## **Overview**
This repository demonstrates **database interaction with PostgreSQL** using a Python application, fulfilling all CRUD (**Create, Read, Update, Delete**) operations for a `students` table. All setup scripts, code, and instructions are included.

---

## **Repository Structure**

```
a3_student_db_comp_3005/
│
├── setup_database.py # Script for automatic DB, schema and data setup
├── setup_students.sql # SQL schema and initial data
├── student_db_app.py # CRUD Python application
└── README.md # This file
```


---

## **Database Schema**

**Table:** `students`

| Field            | Type     | Constraints        |
|------------------|----------|-------------------|
| student_id       | Integer  | Primary Key, Auto-increment |
| first_name       | Text     | Not Null          |
| last_name        | Text     | Not Null          |
| email            | Text     | Not Null, Unique  |
| enrollment_date  | Date     |                   |

**Initial Data:**
- John Doe, `john.doe@example.com`, Enrolled: 2023-09-01
- Jane Smith, `jane.smith@example.com`, Enrolled: 2023-09-01
- Jim Beam, `jim.beam@example.com`, Enrolled: 2023-09-02

---

## **Requirements**
- **PostgreSQL** (local installation or Docker)
- **Python 3.x**
- **psycopg2** Python package  
  _Install with:_  
pip install psycopg2


---

## **Setup Instructions**

### **1. Clone the Repository**
```
git clone https://github.com/SwtPtl/a3_student_db_comp_3005.git
cd a3_student_db_comp_3005
```

### **2. Configure Database Credentials**

- Edit both `setup_database.py` and `student_db_app.py` to change:
  - `DBNAME`, `DBUSER`, `DBPASSWORD`, `DBHOST` (default user `postgres`, password `12345`, host `localhost`)
- Make sure these match your PostgreSQL setup.

### **3. Create the Database and Initialize Schema/Data**
```
python setup_database.py
```

- This script will:
  - Create the target database if it does not already exist
  - Run the SQL script to set up `students` table and insert initial data

OR you can copy paste sql queries from setup_students.sql

### **4. Run the Student Database Application**
```
python student_db_app.py
```

- You will see a menu:
  - **1. List all students**
  - **2. Add a student**
  - **3. Update student email**
  - **4. Delete a student**
  - **5. Exit**

- Enter values as prompted to use each function. Results are displayed in the terminal.

---

## **Application Functions**

- **getAllStudents()**: Displays all student records.
- **addStudent()**: Adds a new student (`first_name`, `last_name`, `email`, `enrollment_date`).
- **updateStudentEmail()**: Changes the email of the student with a given `student_id`.
- **deleteStudent()**: Removes the student record with the provided `student_id`.

Each operation is handled interactively and prints updated results for verification.

---

## **Video Demonstration**

[**Watch here**  ](https://youtu.be/Wc5HebbHmAo)
