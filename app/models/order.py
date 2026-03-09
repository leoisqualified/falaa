# app/models/order.py
from __future__ import annotations

import enum
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class OrderStatus(str, enum.Enum):
    PENDING_PAYMENT = "pending_payment"
    ESCROW = "escrow"
    RELEASED = "released"
    CANCELLED = "cancelled"


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
    )

    seller_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    rider_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    buyer_name: Mapped[str] = mapped_column(String(120))
    buyer_phone: Mapped[Optional[str]] = mapped_column(String(20))

    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))

    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus),
        default=OrderStatus.PENDING_PAYMENT,
        index=True
    )

    handshake_code: Mapped[Optional[str]] = mapped_column(String(4))

    payment_provider: Mapped[Optional[str]] = mapped_column(String(50))

    payment_reference: Mapped[Optional[str]] = mapped_column(String(120), unique=True, index=True)

    is_released: Mapped[bool] = mapped_column(Boolean, default=False)

    escrowed_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    released_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

    seller_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))
    rider_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))
    falaa_fee: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    product = relationship("Product", back_populates="orders")

    seller = relationship(
        "User",
        back_populates="seller_orders",
        foreign_keys=[seller_id],
    )

    rider = relationship(
        "User",
        back_populates="rider_orders",
        foreign_keys=[rider_id],
    )