import requests

from bs4 import BeautifulSoup


url = 'https://www.google.com/'
requests_for_soup = requests.get(url)
soup = BeautifulSoup(requests_for_soup.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))