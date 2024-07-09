from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy metadata and Base class
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# Example model
class ExampleModel(Base):
    __tablename__ = 'example_model'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
