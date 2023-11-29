from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

#basic_info table
class Basic_info(Base):

    __tablename__ = 'basic_info'
    __table_args__ = {'schema':'student'}

    id = Column(Integer,primary_key=True ,autoincrement=True)
    name = Column(String,nullable=False)
    course_id = Column(Integer,nullable=True)



