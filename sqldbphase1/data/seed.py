import sqlite3
import os
from app.orm import ORM
from app.student import Student
from app.campus import Campus

DIR = os.path.dirname(__file__)
DBNAME = 'data/school.db'
DBPATH = os.path.join(DIR, DBNAME)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath
    new_york = Campus(state='New York', city='New York')
    new_york.save()
