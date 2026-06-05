from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Activities Table
class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String, nullable=False)
    external_id = Column(String, unique=True, nullable=True) 
    activity_type = Column(String, nullable=False) 
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Float, nullable=False)

# Sleep Sessions Table
class SleepSession(Base):
    __tablename__ = 'sleep_sessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    total_sleep_minutes = Column(Float, nullable=False)

# HRV Readings Table
class HRVReading(Base):
    __tablename__ = 'hrv_readings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, unique=True)
    hrv_ms = Column(Float, nullable=False)

# Nutrition Logs Table
class NutritionLog(Base):
    __tablename__ = 'nutrition_logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    food_name = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    protein_g = Column(Float, default=0.0)

# Body Metrics Table
class BodyMetric(Base):
    __tablename__ = 'body_metrics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    weight_kg = Column(Float, nullable=True)
    resting_hr = Column(Float, nullable=True)
    vo2max = Column(Float, nullable=True)

# --- DB GENERATOR ---
if __name__ == "__main__":
    import os
    from pathlib import Path
    
    # Get the directory where models.py is located
    BASE_DIR = Path(__file__).resolve().parent
    db_path = BASE_DIR / "health_warehouse.db"

    # This creates the SQLite file in the same folder as models.py
    engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    print(f"Success! Schema defined and {db_path} generated.")