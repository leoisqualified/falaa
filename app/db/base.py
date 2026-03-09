# app/db/base.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models import user, product, order, wallet