import sqlite3
from app.orm import ORM
import os
# DIR = os.path.dirname(__file__)
# DBFILENAME = 'data/school.db'
# DBPATH = os.path.join(DIR, DBFILENAME)

class Campus(ORM):
    tablename = 'campuses'
    fields = ['state', 'city']
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.state = kwargs.get('state')
        self.city = kwargs.get('city')