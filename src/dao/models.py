from sqlalchemy import Column, Integer, String, Boolean, DateTime,create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime, UTC

Base = declarative_base()

class User(Base): 
    __tablename__="Echofrost_Users"
 
    telegram_id= Column(Integer, primary_key=True) #ID пользователя телеграм 
    username=Column(String(50), nullable=True) # @username (None- если скрыт)
    first_name=Column(String(50),nullable=True) # Имя
    last_name=Column(String(50),nullable=True) # Фамилия (None- если нет)
    phone=Column(String(20),nullable=True) # Телефон (Eсли предоставит)
    is_admin=Column(Boolean, default=False) # Админ/нет
    is_active=Column(Boolean, default=False) # Активен ли аккаунт?
    registrated_at= Column(DateTime, default=datetime.now(tz=UTC)) #Дата регистрации

    def __repr__(self):
        return f"<User (id{self.telegram_id}, username='{self.username})'>"
    
engine = create_engine('sqlite:///EchoFrost.db', echo=True)
Base.metadata.create_all(engine)    