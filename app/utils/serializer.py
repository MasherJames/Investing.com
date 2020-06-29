def serialize_company(company):
    ''' Custom company serializer '''
    return {
        "id": company.id,
        "name": company.name
    }


def serializer_historical_data(data):
    ''' Serialize historical data '''

    return {
        "id": data.id,
        "date": data.date,
        "price": data.price,
        "open_price": data.open_price,
        "highest_price": data.highest_price,
        "lowest_price": data.lowest_price,
        "volume": data.volume,
        "percentage_change": data.percentage_change,
        "company": serialize_company(data.company)
    }
