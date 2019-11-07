from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Products(Base):
   __tablename__ = 'Products'
   id = Column(Integer, primary_key=True)
   Name = Column(String)
   Price = Column(Float)
   Picture_Link = Column(String)
   Description = Column(String)


