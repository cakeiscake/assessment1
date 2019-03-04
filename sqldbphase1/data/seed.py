import os
from app.orm import ORM
from app.campus import Campus
from app.student import Student
DIR = os.path.dirname(__file__)
DBNAME = 'school.db'
DBPATH = os.path.join(DIR, DBNAME)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath

    new_york = Campus(state='ny', city='ny')
    new_york.save()
    Locket = Student(campuspk = new_york.pk, first_name='test', last_name='testname', gpa=3.0)
    Locket.save()