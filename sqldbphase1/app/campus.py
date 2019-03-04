from app.orm import ORM
import os
DIR = os.path.dirname(__file__)
DBFILENAME = 'data/school.db'
DBPATH = os.path.join(DIR, DBFILENAME)

class Campus(ORM):
    tablename = 'campuses'
    fields = ['city', 'state']
    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.first_name = kwargs.get('city')
        self.last_name = kwargs.get('state')