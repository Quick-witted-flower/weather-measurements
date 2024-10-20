from sqlalchemy import create_engine, Column, String, Float, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pandas as pd

def main():
    engine = create_engine('sqlite:///measurements.db')
    print("Database engine created successfully.")

    Base = declarative_base()

    class Station(Base):
        __tablename__ = 'stations'
        station = Column(String, primary_key=True)
        name = Column(String)
        latitude = Column(Float)
        longitude = Column(Float)
        elevation = Column(Float)
        country = Column(String)
        state = Column(String)

    class Measurement(Base):
        __tablename__ = 'measurements'
        id = Column(Integer, primary_key=True, autoincrement=True)
        station_id = Column(String)
        date = Column(Date)
        precip = Column(Float)
        tobs = Column(Float)

    Base.metadata.create_all(engine)
    print("Tables created successfully.")

    stations_df = pd.read_csv('clean_stations.csv')
    measurements_df = pd.read_csv('clean_measure.csv')

    stations_df.to_pickle('stations.pkl')
    measurements_df.to_pickle('measurements.pkl')

    print("Data loaded from CSV and saved to pickle files.")

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        stations = []
        for index, row in stations_df.iterrows():
            existing_station = session.query(Station).filter_by(station=row['station']).first()
            if not existing_station:
                station= Station(
                    station=row['station'],
                    name=row['name'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                    elevation=row['elevation'],
                    country=row['country'],
                    state=row['state']
                )
                stations.append(station)

        if stations:
            session.add_all(stations)
            session.commit()

        measurements = []
        for index, row in measurements_df.iterrows():
            try:
                measurement_date = datetime.strptime(row['date'], '%Y-%m-%d')
            except ValueError:
                continue

            measurement = Measurement(
                station_id=row['station'],
                date=measurement_date,
                precip=row['precip'],
                tobs=row['tobs']
            )
            measurements.append(measurement)

        session.add_all(measurements)
        session.commit()
        print("Data inserted into the database.")

        result = engine.execute("SELECT * FROM stations LIMIT 5").fetchall()
        for row in result:
            print(row)
    
    finally:
        session.close()

if __name__ == "__main__":
    main()

    
