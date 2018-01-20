from bs4 import BeautifulSoup
import requests
url = "https://akshatmittal.com/youtube-realtime/#!/UC9z7EZAbkphEMg0SP7rw44A"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

digits = soup.find_all(class="odometer-value")