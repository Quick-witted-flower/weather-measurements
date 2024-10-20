# Weather Stations Database with SQLAlchemy

This project demonstrates how to use SQLAlchemy ORM to create a SQLite database from CSV files containing weather station and measurement data. It includes:

1. Creating a SQLite database engine.
2. Defining table structures using SQLAlchemy ORM.
3. Loading data from CSV files.
4. Inserting the data into the database.
5. Running a simple query to fetch data from the database.

## Project Structure

- `engine.py`: Initializes the SQLite database engine.
- `define_models.py`: Defines the database tables (ORM models) for weather stations and measurements.
- `load_data.py`: Loads data from CSV files (`clean_stations.csv` and `clean_measure.csv`) and saves them in pickle format.
- `insert_data.py`: Inserts the data from pickle files into the SQLite database.
- `query_data.py`: Executes a query to retrieve records from the `stations` table.

## Requirements

To run this project, you need the following Python packages:

- `sqlalchemy`
- `pandas`

You can install the required packages by running:

```bash
pip install sqlalchemy pandas

## Data Files

The project expects two CSV files:

- **clean_stations.csv**: Contains data about weather stations (station ID, name, latitude, longitude, etc.).
- **clean_measure.csv**: Contains measurement data (station ID, date, precipitation, temperature, etc.).

Ensure these files are present in the project directory.

## How to Run the Project

1. Clone or download the project to your local machine.
2. Place the CSV files (`clean_stations.csv` and `clean_measure.csv`) in the same directory as the Python scripts.
3. Run the script to create the database, load data, and insert it into the database:

```bash
python your_script_name.py

This will:

- Create the SQLite database `measurements.db`.
- Define the tables `stations` and `measurements`.
- Load data from the CSV files and insert it into the database.
- Query the database to retrieve and display the first five records from the `stations` table.
