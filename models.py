import datetime

from sqlalchemy import Column, String, Integer, create_engine, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+pymysql://root:qwerty@localhost:33061/company"
)
Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    salary = Column(Float, default=0, nullable=False)
    creation_date = Column(
        DateTime,
        default=datetime.datetime.now,
        nullable=False
    )

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name}, {self.email})"


Base.metadata.create_all()