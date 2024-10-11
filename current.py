from sqlalchemy import Column, String, Integer, Date

from base import Base


class Current(Base):
    __tablename__ = 'currents'

    id = Column(Integer, primary_key=True)
    location = Column(String)
    reading = Column(String)

    def __init__(self, location, reading):
        self.location = location
        self.reading = reading