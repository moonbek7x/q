from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from dotenv import load_dotenv
from sqlalchemy import BigInteger
from os import getenv

load_dotenv()

DB_URL = getenv('DB_URL')
ASYNC_DB_URL = getenv('ASYNC_DB_URL')

if not DB_URL:
    raise ValueError('DB_URL not found')
if not ASYNC_DB_URL:
    raise ValueError('ASYNC_DB_URL not found')

engine = create_engine(DB_URL)
async_engine = create_async_engine(ASYNC_DB_URL)

Sessiomlocal = sessionmaker(bind= engine)
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine, expire_on_commit=False, class_=AsyncSession
)




class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, autoincrement=True)

def get_db():
    db= Sessiomlocal()
    try:
        yield db
    finally:
        db.close()

async def get_async_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            print(session)
            raise
        finally:
            await session.close()











