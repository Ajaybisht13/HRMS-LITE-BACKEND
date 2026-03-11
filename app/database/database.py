from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://hrms_lite_6gb8_user:XMdNEgaorJAKpKPJoyXKqVSAHdQobzWS@dpg-d6ord9ma2pns73b0lo90-a.oregon-postgres.render.com/hrms_lite_6gb8"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()