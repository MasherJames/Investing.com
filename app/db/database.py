from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = None


def init_db():
    '''
        - Initialise the db.
        - Import all models here to be registered properly on the metadata
    '''

    try:
        engine = create_engine(current_app.config.get('DATABASE_URL'))

        import app.db.models
        Base.metadata.create_all(bind=engine)

        return db_session

    except Exception as err:
        print(err)


db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
