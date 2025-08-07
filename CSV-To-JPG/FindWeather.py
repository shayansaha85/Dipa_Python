import requests  # Import the requests library to make HTTP requests
import pandas as pd  # Import pandas for data manipulation


def findTemparature(city):
      # Make a GET request to OpenWeatherMap Geocoding API to get latitude and longitude for the city
      response = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=*****************************",
            headers={'Content-Type': 'application/json'}
      )

      res = response.json()  # Parse the JSON response
      res_object = res[0]  # Get the first result (city info)

      lat = res_object['lat']  # Extract latitude
      lon = res_object['lon']  # Extract longitude

      # Make a GET request to OpenWeatherMap Weather API to get weather data for the coordinates
      weather_Response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid=*****************************"
      )

      temperature = weather_Response.json()['main']['temp']  # Extract temperature in Celsius
      return temperature  # Return the temperature


df = pd.read_csv('cityNames.csv')  # Read city names from a CSV file
cityNames = list(df['CityName'])  # Convert the 'CityName' column to a list

# Prepare a dictionary to store city names and their temperatures
new_csv_data = { 
      'city_names': [],
      'temperature': []
}

# For each city, get the temperature and store it in the dictionary
for city in cityNames:
      temp = findTemparature(city)  # Get temperature for the city
      new_csv_data['city_names'].append(city)  # Add city name to the list
      new_csv_data['temperature'].append(temp)  # Add temperature to the list
      print(f'** Task completed for city : {city}')  # Print progress

outputCsvPath = 'output/cityWithTemperature.csv'  # Output CSV file path

cityWithTemperature = pd.DataFrame(new_csv_data)  # Create a DataFrame from the dictionary
cityWithTemperature.to_csv(outputCsvPath, index=False)  # Save the DataFrame