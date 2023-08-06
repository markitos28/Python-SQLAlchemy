from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mssql://DESKTOP-LFB6P0N/Staging?trusted_connection=yes", echo=True)

def SessionSQLServer():
    Session= sessionmaker(engine)
    session = Session()
    return session

