from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Courses(Base):

    __tablename__ = 'courses'
    __table_args__ = {'schema':'student'}

    id = Column(Integer,primary_key=True)
    course_name = Column(String,nullable=False)
