import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine


DATABASE_URL = "sqlite+aiosqlite:///blog.db"

metadata = sa.MetaData()
engine = create_async_engine(DATABASE_URL)