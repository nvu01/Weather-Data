# Create a table in SQLite using the SQLAlchemy ORM
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Create a SQLite database named "my_database" and set up a session using sessionmaker to allow interacting with the database.
engine = create_engine('sqlite+pysqlite:///my_database.db', echo=True)

Session = sessionmaker(engine)

class Base (DeclarativeBase):
    pass

# Create a class that represents a table named "Weather_Data"
class WeatherData(Base):
    __tablename__ = 'Weather_Data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)
    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    avg_windsp = Column(Float)
    min_windsp = Column(Float)
    max_windsp = Column(Float)
    sum_precip = Column(Float)
    min_precip = Column(Float)
    max_precip = Column(Float)

Base.metadata.create_all(engine)

# Populate the table with the weather data
def add_record(latitude, longitude, month, day, year):
    with Session() as session:
        from W_class import W
        instance = W(latitude, longitude, month, day, year)
        instance.aggregate()

    # Check for the existence of a record to avoid duplicating rows.
        existing_data = session.query(WeatherData).filter(
            WeatherData.latitude == instance.latitude,
            WeatherData.longitude == instance.longitude,
            WeatherData.month == instance.month,
            WeatherData.day == instance.day,
            WeatherData.year == instance.year
        ).first()

    # If no matching record is found, then a new record will be added
        if not existing_data:
            new_row = WeatherData (
                latitude = instance.latitude,
                longitude = instance.longitude,
                month = instance.month,
                day = instance.day,
                year = instance.year,
                avg_temp = instance.avg_temp,
                min_temp = instance.min_temp,
                max_temp = instance.max_temp,
                avg_windsp = instance.avg_windsp,
                min_windsp = instance.min_windsp,
                max_windsp = instance.max_windsp,
                sum_precip = instance.sum_precip,
                min_precip = instance.min_precip,
                max_precip = instance.max_precip
            )
            session.add(new_row)
            session.commit()
            print('New record is added.')
        else:
            print('Record already exists.')

# Query all records in the table
def display_last_record():
    with (Session() as session):
        last_record = session.query(WeatherData).order_by(WeatherData.id.desc()).first()
        if last_record is None:
            result = f'Weather_Data table has no record!'
        else:
            result = (f'ID: {last_record.id}, Latitude: {last_record.latitude}, Longitude: {last_record.longitude}, Month: {last_record.month}, Date: {last_record.day}, Year: {last_record.year}, '
                      f'Avg Temp: {last_record.avg_temp}, Min Temp: {last_record.min_temp}, Max Temp: {last_record.max_temp}, '
                      f'Avg Wind Speed: {last_record.avg_windsp}, Min Wind Speed: {last_record.min_windsp}, Max Wind Speed: {last_record.max_windsp}, '
                      f'Sum Precipitation: {last_record.sum_precip}, Min Precipitation: {last_record.min_precip}, Max Precipitation: {last_record.max_precip}')
        print(result)

# Query the most currently added record
def display_all_records():
    with Session() as session:
        all_data = session.query(WeatherData).all()
        if not all_data:
            result = f'Weather_Data table has no record!'
        else:
            records = []
            for record in all_data:
                records.append(f'ID: {record.id}, Latitude: {record.latitude}, Longitude: {record.longitude}, Month: {record.month}, Date: {record.day}, Year: {record.year}, '
                               f'Avg Temp: {record.avg_temp}, Min Temp: {record.min_temp}, Max Temp: {record.max_temp}, '
                               f'Avg Wind Speed: {record.avg_windsp}, Min Wind Speed: {record.min_windsp}, Max Wind Speed: {record.max_windsp}, '
                               f'Sum Precipitation: {record.sum_precip}, Min Precipitation: {record.min_precip}, Max Precipitation: {record.max_precip}')
            result = "\n".join(records)
        print(result)

# Delete all records in the table
def delete_all():
    with Session() as session:
        session.query(WeatherData).delete()
        session.commit()
        print("All records have been deleted.")

# Test all the functions
if __name__ == "__main__":
    with Session() as session:
        display_last_record()
        display_all_records()
        add_record(30, 80.5, 10, 5, 2024)
        add_record(30, 80.5, 10, 5, 2023)
        display_last_record()
        display_all_records()
        delete_all()

# Another way to check the database is to go on the website sqliteviewer.app
# This is a tool to help you visualize all the tables in a SQLite database.
# User only need to upload .db file to sqliteviewer.app
