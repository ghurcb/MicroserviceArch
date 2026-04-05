from __future__ import annotations
import os


def get_database_url() -> str:
    url = os.getenv("ASYNC_DATABASE_URL")
    if not url:
        raise RuntimeError(
            "ASYNC_DATABASE_URL is not set."
        )
    return url


