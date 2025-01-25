from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from models.base import Base


DATABASE_URL = 'sqlite+aiosqlite:///./weather.db'

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def init_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()