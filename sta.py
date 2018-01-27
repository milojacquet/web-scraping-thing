from bs4 import BeautifulSoup
import requests
import re
import os
from datetime import datetime
import time
def count(user):
	url = "https://socialblade.com/youtube/user/"+user+"/realtime"
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	#print(soup)
	digits = soup.find(id="rawCount")
	#digits = soup.find_all("span", attrs={"class": "odometer-value"})
	#print(type(digits))
	#return re.findall(r"\d+", digits).group(0)
	return str(digits.string)

def log(user, n, t):
	mode = "a" if os.path.isfile("./"+user+".csv") else "w"
	with open("./"+user+".csv", mode) as f:
		for i in range(n):
			#f.write(str(datetime.now())+","+count(user)+"\n")
			f.write(str(i)+"\n")
			print(i)
			time.sleep(t)

log("carykh", 100, 2)
