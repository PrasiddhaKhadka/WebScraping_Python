from bs4 import BeautifulSoup
import requests

url = "https://timesofindia.indiatimes.com/sports/cricket/ipl/schedule"

def fetchAndSaveToFile(url,path):
    r = requests.get(url)
    with open(path, 'w') as f:
        f.write(r.text)
    


fetchAndSaveToFile(url, "data/ipl_schedule.html")
# response = requests.get(url)

# print(response.text)