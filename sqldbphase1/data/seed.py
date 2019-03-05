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
    new_york = Campus(state='New York', city='New York')
    houston = Campus(state='Texas', city='Houston')
    new_york.save()
    houston.save()
        
    walker = Student(campus_pk=new_york.pk, first_name='Walker', last_name='Locket',studentID=genID(), gpa=3.1)
    casey = Student(campus_pk=new_york.pk, first_name='Casey', last_name='Walker',studentID=genID(), gpa=2.7)
    frank = Student(campus_pk=new_york.pk, first_name='Franklyn', last_name='Kilome',studentID=genID(), gpa=3.8)
    hecton = Student(campus_pk=new_york.pk, first_name='Hecton', last_name='Santiago',studentID=genID(), gpa=2.9)
    walker.save()
    casey.save()
    frank.save()
    hecton.save()

    framber = Student(campus_pk=houston.pk, first_name='Framber', last_name='Valdez', studentID=genID(), gpa=3.9)
    brad = Student(campus_pk=houston.pk, first_name='Brad', last_name='Peacock', studentID=genID(), gpa=2.8)
    reymin = Student(campus_pk=houston.pk, first_name='Guduan', last_name='Reymin', studentID=genID(), gpa=3.5)
    gerrit = Student(campus_pk=houston.pk, first_name='Cole', last_name='Gerrit', studentID=genID(), gpa=3.0)
    framber.save()
    brad.save()
    reymin.save()
    gerrit.save()
