from databases import Database
from sqlalchemy import create_engine, MetaData
import os
from src.config import DATABASE_URL
from src.database.models import Base

# Initialize the database
database = Database(DATABASE_URL)
metadata = MetaData()

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
