# app/models/wallet.py
from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True, index=True
    )

    balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)

    escrow_balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)

    total_earned: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)

    currency: Mapped[str] = mapped_column(String(10), default="GHS")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    user = relationship("User", back_populates="wallet")