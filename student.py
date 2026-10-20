from database import base
from sqlalchemy import Colum, String, Integer

class Student(base):
    __tablename__="students"
    __table_args__={"schema":"training"}

    id=Colum(Integer, primary_key=True, autincrement=True)
    name=Colum(String[50])