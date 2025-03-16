from sqlalchemy import select


from database.postgres.database import get_async_db
from database.postgres.models import User

import asyncio

async def create_user():
    async for session in get_async_db():
        new_user = User(
            first_name = 'aybek',
            age = 14,
            phone = '+998785627977'
        )
        session.add(new_user)
        await session.commit()
        
async def read_user():
     async for db in get_async_db(): 
         db_user = (await db.execute(select(User).where(User.first_name == 'aybek'))).scalars().first()
         if db_user:
             print(db_user.age)
async def main():
# #     await create_user()
    await read_user()
asyncio.run(main=main())