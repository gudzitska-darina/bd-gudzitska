from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

from base import Base


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    credits = Column(Integer)

    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
