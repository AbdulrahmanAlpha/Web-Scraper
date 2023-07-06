import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send an HTTP request to the website
url = 'https://www.example.com'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find('div', {'class': 'content'}).text

# Store the extracted data in a structured format
df = pd.DataFrame({'data': [data]})
df.to_csv('data.csv', index=False)