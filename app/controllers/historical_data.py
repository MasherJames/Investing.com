from sqlalchemy.exc import SQLAlchemyError

from app.db.models import HistoricalData, Company
from app.db.database import db_session
from app.utils.serializer import serializer_historical_data, serialize_company


class HistoricalDataController:

    @staticmethod
    def get_all_historical_data():
        ''' Get all historical data from the database '''
        session = db_session()
        try:
            all_data = session.query(HistoricalData).all()
            if len(all_data) == 0:
                return {
                    "status": False,
                    "message": "There is no data for now",
                    "historical_data": []
                }
            result = []
            for data in all_data:
                company = session.query(Company).filter_by(
                    id=data.company_id).first()
                setattr(data, 'company', company)
                result.append(serializer_historical_data(data))
            return {
                "status": True,
                "message": "Successfully retrieved data",
                "historical_data": result
            }
        except SQLAlchemyError as err:
            # rollback the transaction if something fails
            print(err)
            session.rollback()
            raise
        finally:
            # close the Session and reset any existing SessionTransaction state
            session.close()

    @staticmethod
    def get_company_historical_data(company_name):
        ''' Get historical data for a specific company '''
        session = db_session()
        try:
            company = Company.query.filter(
                Company.name == company_name).first()
            if company is not None:
                all_data = session.query(HistoricalData).filter_by(
                    company_id=company.id).all()
                if len(all_data) == 0:
                    return {
                        "status": False,
                        "message": "There is no data for now",
                        "historical_data": []
                    }
                result = []
                for data in all_data:
                    setattr(data, 'company', company)
                    result.append(serializer_historical_data(data))
                return {
                    "status": True,
                    "message": "Successfully retrieved data",
                    "historical_data": result
                }
        except SQLAlchemyError as err:
            # rollback the transaction if something fails
            print(err)
            session.rollback()
        finally:
            # close the Session and reset any existing SessionTransaction state
            session.close()
