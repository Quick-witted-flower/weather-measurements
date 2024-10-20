             Weather Stations Database with SQLAlchemy

## Table of Contents
* #general-information
* #technologies-used
* #usage
* #setup
* #contact

### General Information
This project was completed as part of an assignment with the following task: 
Use the datasets `clean_stations.csv` and `clean_measure.csv`. Based on these datasets, create a database and a table that can be queried, for example with the following command:**
```python
conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
The purpose of the project is to load the weather station and measurement data from CSV files, store them in a SQLite database, and provide a method for querying the data using SQLAlchemy.

### Technologies Used
- **Python** - version 3.8+
- **SQLAlchemy** - version 1.4+
- **Pandas** - version 1.3+
- **SQLite** - lightweight SQL database

### Setup
    Requirements:
All the dependencies are listed in the `requirements.txt` file. To install the required dependencies, run the following command:
    ```bash
    pip install -r requirements.txt

    Installation:
1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <project-directory>

2. Install dependencies:
Install the required libraries listed in the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt

3. Prepare CSV files:
Ensure that `clean_stations.csv` and `clean_measure.csv` are available in the project directory, containing the relevant weather data.

4. Run the script:
Execute the Python script to load the data into the database and generate the pickle files:

```bash
python main.py

###Contact 
Created by @Quick-witted-flower - feel free to contact me!



