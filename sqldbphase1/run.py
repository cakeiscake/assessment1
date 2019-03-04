from data.schema import schema
from data.seed import seed
from app.orm import ORM
import os

DIR = os.path.dirname(__file__)
DBFILENAME = 'data/school.db'
DBPATH = os.path.join(DIR, 'data', DBFILENAME)
if __name__ =='main':
    ORM.dbpath = DBPATH
    schema()
    seed()
