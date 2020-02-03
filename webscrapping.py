import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.936809930030805&lon=-118.24893999999995#.XQz-qnHhVPY')

soup = BeautifulSoup(page.content,'html.parser')

week = soup.find(id="seven-day-forecast-body")
# print(week)
items = week.find_all(class_="tombstone-container")

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp temp-high').get_text())

period = [item.find(class_='period-name').get_text() for item in items]

short_desc = [item.find(class_='short-desc').get_text() for item in items]

temperature = [item.find(class_='temp').get_text() for item in items]

# print(period)
# print(short_desc)
# print(temperature)

weather_stuff = pd.DataFrame(
  {
    'period': period,
    'short-desc': short_desc,
    'temperatures': temperature,
  }
)
print(weather_stuff)
weather_stuff.to_csv('weather.csv')























  
