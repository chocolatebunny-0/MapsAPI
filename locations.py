import googlemaps
import pandas as pd
import requests
from datetime import datetime


with open('apikey.txt') as f:
    api_key = f.readline()
    f.close



r_cols = ['id', 'university names', 'country code']
#loading the data into a pandas datafram 
df = pd.read_csv('university-names.csv' )
print(df.head())
print('............................................................')
print(df.info())
print('............................................................')
df = df.iloc[:, :]


for index, row in df.iterrows():
   query = row['university names']
   print('Getting ', index, 'of 5890')
   url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=formatted_address&key={}'.format(query, api_key)
   response = requests.get(url)
   response.encoding = 'utf-8'
   result = response.json()
   address = result.get('candidates')[0].get('formatted_address')  
   print(address)
   df.loc[index, 'address'] = address
   print('............................................................')
df.drop_duplicates(['university names'], keep='first', inplace=True)
print(df)


export_csv = df.to_csv (r'C:\Users\Sodei\Desktop\University_Locations.csv', index = None, header=True) 
