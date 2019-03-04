from data.schema import schema
from data.seed import seed
from app.orm import ORM


# DIR = os.path.dirname(__file__)
# DBFILENAME = 'data/school.db'
# DBPATH = os.path.join(DIR, DBFILENAME)
# ORM.dbpath = DBPATH
schema()
seed()