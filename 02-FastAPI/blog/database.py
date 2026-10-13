import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine
from config import settings


metadata = sa.MetaData()
engine = create_async_engine(settings.database_url)