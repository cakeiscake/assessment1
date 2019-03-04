from app.orm import ORM
import os
DIR = os.path.dirname(__file__)
DBFILENAME = 'data/school.db'
DBPATH = os.path.join(DIR, DBFILENAME)

class Student(ORM):
    tablename = 'students'
    fields = ['first_name', 'last_name', 'GPA']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last name')
        self.gpa = kwargs.get('GPA')