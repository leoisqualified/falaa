# app/models/product.py
from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    seller_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    image_url: Mapped[Optional[str]] = mapped_column(String(500))

    magic_link_code: Mapped[str] = mapped_column(String(64), unique=True, index=True)

    group_target: Mapped[Optional[int]] = mapped_column(Integer)
    discount_percentage: Mapped[Optional[Decimal]] = mapped_column(Numeric(5, 2))

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    seller = relationship("User", back_populates="products")

    orders = relationship("Order", back_populates="product")