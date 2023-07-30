from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = config('DB_URL')

engine = create_engine(DB_URL, pool_pre_ping=True)
SessaoBD = sessionmaker(autocommit=False, autoflush=False, bind=engine)
