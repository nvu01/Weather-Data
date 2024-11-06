# Historical Weather Data Project

This Python program collects historical weather information for a specific location and date from the last five years.
Weather data is retrieved from Open Meteo API. The data set includes mean temperature, max wind speed, and total precipitation for a chosen location and date in each of the five years. 
The program stores the weather data in a local database named "my_database". The program can also query or delete records of weather data from this database.

## Installation

Install the required packages listed in requirements.txt

## Usage 

To run the program, import the main.py file into another Python script and call its functions to interact with the Weather_Data table.

### Commands
Use the following code to import main.py and its functions:  
from main import add_record, display_last_record, display_all_records, delete_all

Call the following funtions to interact with the weather data logging system:
1. The __add_record__ function retrieves weather data for a specified location and date (see Inputs section), aggregates it, and saves it to the database.
2. The __display_last_record__ function displays the most recetly added record
3. The __display_all_records__ function displays all the records in the Weather_Data table
4. The __delete_all__ function delete all records in the Weather_Data table

### Inputs

To add a record using add_record function, specify inputs for the following parameters:
- Latitude: Latitude of the location (e.g., 30).
- Longitude: Longitude of the location (e.g., 80.5).
- Month: Month for which data is fetched (e.g., 10 for October).
- Day: Day of the month (e.g., 5).
- Year: Year for which data is fetched (e.g., 2024).

Examples of how to call the add_record function:

- Example 1:  
latitude = 30  
longitude = 80.5  
month = 10  
day = 5  
year = 2024  
add_record(latitude, longitude, month, day, year)


- Example 2:  
add_record(30,80.5,10,5,2024)

### Outputs

When the __add_record__ funtion is called, weather data is retrieved and saved to my_database.db. The program returns "New record is added." message.  
If the added record already exists, the program will return "Record already exists." message.

When the __display_last_record__ or __display_all_records__ functions are called, the program outputs records in the Weather_Data table with the following information:

- Record ID
- Latitude
- Longitude
- Month
- Day
- Year
- Aggregated statistics including:
  - Average temperature
  - Minimum temperature
  - Maximum temperature
  - Average wind speed
  - Minimum wind speed
  - Maximum wind speed
  - Total precipitation
  - Minimum precipitation
  - Maximum precipitation 

If there is no record in the table, the program returns the message: "Weather_Data table has no record!"

When the __delete_all__ functions are called, the program deletes all records in the table and returns the message: "All records have been deleted"
