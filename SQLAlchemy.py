import psycopg2
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
import faker

engine = create_engine("postgresql+psycopg2://postgres:pipneinstall229@localhost")

Base = declarative_base()
class Users(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, nullable=False)
  name = Column(String(250), nullable=False)
  hp = Column(Integer, default=100)
  damage = Column(Integer, default=20)
Session = sessionmaker(bind=engine)
s=Session()
Base.metadata.create_all(engine)
#user = Users(name = 'Roma')
#s.add(user)
#s.commit()
fake = faker.Faker('ru-RU')
for ne_i in range(100):
  user = Users(name=fake.first_name())
  s.add(user)
  s.commit()
data = s.query(Users).filter(Users.name=='Roma').all()
for ne_i_a_user in data:
  print(ne_i_a_user.__dict__)


























































#import psycopg2
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import Column, Integer, String
#from sqlalchemy import create_engine
#from sqlalchemy.orm import declarative_base
#anegine = create_engine("postgresql+psycopg2://root:pipneinstall229@localhost/tablica2")
#
#
#Base = declarative_base()
#class Users(Base):
#    __tablename__ = 'users'
#    id = Column(Integer, primary_key=True, nullable=False)
#    name = Column(String(250), nullable=False)
#    hp = Column(Integer, default=100)
#    damage = Column(Integer, default=20)
#Base.metadata.create_all(anegine)
#Session = sessionmaker(bind=anegine)
#s = Session()
