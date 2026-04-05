from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base

if TYPE_CHECKING:
    from .user import User
    from .article import Article


class Comment(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    article_id: Mapped[int] = mapped_column(ForeignKey("article.id", ondelete="CASCADE"), index=True, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True, nullable=False)
    article: Mapped["Article"] = relationship(back_populates="comments")
    author: Mapped["User"] = relationship(back_populates="comments")
