from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

from base import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    faculty = Column(String)
    student_number = Column(Integer)

    def __init__(self, name, faculty, student_number):
        self.name = name
        self.faculty = faculty
        self.student_number = student_number
