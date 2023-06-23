from ...extensions.extensions import Base
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass
from typing import Optional


@dataclass
class User(Base):
    __tablename__ = 'users'
    email: str = Column(String(120), unique=True)
    id: Optional[int] = Column(Integer, primary_key=True)
