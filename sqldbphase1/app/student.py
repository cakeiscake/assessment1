import sqlite3
from app.orm import ORM
import os
DIR = os.path.dirname(__file__)
DBFILENAME = 'data/school.db'
DBPATH = os.path.join(DIR, DBFILENAME)

class Student(ORM):
    tablename = 'students'
    fields = ['campus_pk', 'studentID', 'first_name', 'last_name', 'gpa']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.campus_pk = kwargs.get('campus_pk')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.studentID = kwargs.get('studentID')
        self.gpa = kwargs.get('gpa')
    