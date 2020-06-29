from sqlalchemy.exc import SQLAlchemyError

from app.db.models import Company
from app.db.database import db_session
from app.utils.serializer import serialize_company


class CompanyController:

    @staticmethod
    def get_all_companies():
        ''' Get all companies '''
        session = db_session()
        try:
            companies = session.query(Company).all()
            if len(companies) == 0:
                return {
                    "status": False,
                    "message": "There a re no companies for now",
                    "companies": []
                }
            return {
                "status": True,
                "message": "Successfully retrieved companies",
                "companies": [serialize_company(company) for company in companies]
            }
        except SQLAlchemyError as err:
            # rollback the transaction if something fails
            print(err)
            session.rollback()
            raise
        finally:
            # close the Session and reset any existing SessionTransaction state
            session.close()
