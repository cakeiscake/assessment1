import os
from app.orm import ORM
from app.campus import Campus
from app.student import Student
from app.util import genID
DIR = os.path.dirname(__file__)
DBNAME = 'school.db'
DBPATH = os.path.join(DIR, DBNAME)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath
    studentID = genID()
    new_york = Campus(state='New York', city='New York')
    houston = Campus(state='Texas', city='Houston')
    Locket = Student(first_name='test', last_name='testname',studentID=studentID, gpa=3.0)
    new_york.save()
    houston.save()
    # Locket.save()