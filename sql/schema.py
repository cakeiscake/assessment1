import sqlite3
import os
DBNAME= 'school.db'
DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, DBNAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cursor.execute(DROPSQL.format(tablename='campuses'))

        SQL = """CREATE TABLE campuses(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                students_pk INT,
                state VARCHAR (16) NOT NULL,
                city VARCHAR (32),
                FOREIGN KEY (students_pk) REFERENCES students(pk)
            );"""

        cursor.execute(SQL)

        cursor.execute(DROPSQL.format(tablename='students'))

        SQL = """CREATE TABLE students(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(32),
                last_name VARCHAR(32),
                GPA FLOAT
            );"""
        cursor.execute(SQL)