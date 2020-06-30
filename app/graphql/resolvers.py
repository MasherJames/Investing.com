from app.controllers.company import CompanyController
from app.controllers.historical_data import HistoricalDataController


def resolve_all_companies(*_):
    result = CompanyController.get_all_companies()
    return result


def resolve_all_historical_data(*_):
    result = HistoricalDataController.get_all_historical_data()
    return result


def resolve_company_historical_data(*_, company):
    result = HistoricalDataController.get_company_historical_data(company)
    return result
