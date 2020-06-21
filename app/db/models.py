from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    historicaldata = relationship("HistoricalData", backref="company")

    def __init__(self, name=None):
        ''' Company constructor '''
        self.name = name

    def __repr__(self):
        ''' Object representation on a company '''
        return '<Company %r>' % (self.name)


class HistoricalData(Base):
    __tablename__ = "historicaldata"
    id = Column(Integer, primary_key=True)
    date = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    open_price = Column(Float, nullable=False)
    highest_price = Column(Float, nullable=False)
    lowest_price = Column(Float, nullable=False)
    volume = Column(String(50), nullable=False)
    percentage_change = Column(String(50), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'))

    def __init__(self, date=None,
                 price=None,
                 open_price=None,
                 highest_price=None,
                 lowest_price=None,
                 volume=None,
                 percentage_change=None,):
        ''' HistoricalData constructor '''
        self.date = date
        self.price = price
        self.open_price = open_price
        self.highest_price = highest_price
        self.lowest_price = lowest_price
        self.volume = volume
        self.percentage_change = percentage_change

    def __repr__(self):
        ''' Object representation on historical data '''
        return '<HistoricalData %r>' % (self.date)
