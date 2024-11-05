# Define a class named "W", which represents weather data
class W:
    def __init__(self, latitude, longitude, month, day, year):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None
        self.avg_windsp = None
        self.min_windsp = None
        self.max_windsp = None
        self.sum_precip = None
        self.min_precip = None
        self.max_precip = None

# get_dates method takes class attributes month, day, year and creates dates in format YYYY/MM/DD. The method returns a list of 5 dates that have the same month and day but in 5 different years.
    def get_dates(self):
        dates = []
        for i in range(5):
            year = self.year - i
            date_str = f'{year}-{self.month:02d}-{self.day:02d}'
            dates.append(date_str)
        return dates

# weather_data method retrieves weather data for a specific date and location from Open Meteo API. The method returns a dictionary using json.loads() to parse the JSON string
    def weather_data(self, date):
        import requests
        import json
        url = 'https://archive-api.open-meteo.com/v1/archive'
        params = {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'start_date': date,
            'end_date': date,
            'daily': ['temperature_2m_mean', 'precipitation_sum', 'wind_speed_10m_max']
        }
        response = requests.get(url, params=params)
        return json.loads(response.text)

# temp() method returns mean temperature data for 5 specific dates.
    def temp(self):
        dates = self.get_dates() #This line calls the get_dates method to return a list of dates
        temp_list = [] #An empty list named temp_list is initialized.
        for date in dates: #This block of code iterates over each date in the dates list.
            data = self.weather_data(date) #For each date the weather_data method is called.
            temp = data['daily']['temperature_2m_mean'][0] #This line extracts the mean temperature from the data dictionary
            temp_list.append(temp) #The extracted value is then added to the temp_list
        return temp_list

# windsp() gathers maximum wind speed data for the 5 dates.
    def windsp(self):
        dates = self.get_dates()
        windsp_list = []
        for date in dates:
            data = self.weather_data(date)
            temp = data['daily']['wind_speed_10m_max'][0]
            windsp_list.append(temp)
        return windsp_list

# precip() gathers sum precipitation data for the 5 dates.
    def precip(self):
        dates = self.get_dates()
        precip_list = []
        for date in dates:
            data = self.weather_data(date)
            temp = data['daily']['precipitation_sum'][0]
            precip_list.append(temp)
        return precip_list

# The aggregate method calculates various statistical measures based on the data gathered from previous methods in the class. These aggregate values are then assigned to attributes of the W class.
    def aggregate(self):
        temp_list = self.temp()
        self.avg_temp = round(sum(temp_list)/5, 2)
        self.min_temp = min(temp_list)
        self.max_temp = max(temp_list)
        windsp_list = self.windsp()
        self.avg_windsp = round(sum(windsp_list)/5, 2)
        self.min_windsp = min(windsp_list)
        self.max_windsp = max(windsp_list)
        precip_list = self.precip()
        self.sum_precip = round(sum(precip_list), 2)
        self.min_precip = min(precip_list)
        self.max_precip = max(precip_list)

# Instantiate class W to test the class methods
def instantiate_W(latitude, longitude, month, day, year):
    instance = W(latitude, longitude, month, day, year)

    temp_data = instance.temp()
    print(f'Mean temperature on the chosen day accross the last 5 years: {temp_data}')

    windsp_data = instance.windsp()
    print(f'Max wind speed on the chosen day accross the last 5 years: {windsp_data}')

    precip_data = instance.precip()
    print(f'Precipitation sum on the chosen day accross the last 5 years: {precip_data}')

    instance.aggregate()
    print(f'Average temperature: {instance.avg_temp}°C, Min temperature: {instance.min_temp}°C, Max temperature: {instance.max_temp}°C')
    print(f'Average wind speed: {instance.avg_windsp} mph, Min wind speed: {instance.min_windsp} mph, Max wind speed: {instance.max_windsp} mph')
    print(f'Total precipitation: {instance.sum_precip} in, Min precipitation: {instance.min_precip} in, Max precipitation: {instance.max_precip} in')

if __name__ == '__main__':
    instantiate_W(30,80.5,10,5,2024)

