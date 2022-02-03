from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey

Base = declarative_base()
engine = create_engine("sqlite:///main.db", echo=False)


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    player_name = Column(String, nullable=False, unique=False)


class History(Base):
    __tablename__ = "history"
    id_winner = Column(Integer, primary_key=True)
    player_name = Column(String, unique=False)
    date = Column(DateTime, nullable=False)
    score = Column(Integer, nullable=False)

    def get_points(self):
        return self.score


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


def get_session():
    return session


def delete_table(table):
    table.__table__.drop(engine)
