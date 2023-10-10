import json
import requests

url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c3fc8d32a86f4ab9876325807455e87e"

r = requests.get(url)

news = json.loads(r.text)
# print(news)
for article in news["articles"]:
    print(article["title"])
    print()