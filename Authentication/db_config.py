import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Connection point: This is the runtime connection that your FastAPI app will use to query the database.
load_dotenv(".env")

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"] #creates the actual connection engine to PostgreSQL.

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine)) #sets up a thread-safe session for database operations.
Base = declarative_base() #creates the base class that models inherit from.
Base.query = db_session.query_property() # user = User.query.filter(User.username=='neema').first()
