
from sqlalchemy.orm import  mapped_column, Mapped
from sqlalchemy.sql import func



from database.postgres.database import Base , engine
 
import datetime
from typing import Optional
class User(Base):
    __tablename__ = 'users'

    first_name:Mapped[str]
    last_name:Mapped[Optional[str]]
    age:Mapped[int]
    phone:Mapped[str] = mapped_column(unique=True)

    at:Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    up_at:Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
print('ishlayapti')

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)



















