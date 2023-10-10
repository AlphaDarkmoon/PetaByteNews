from django.shortcuts import render

import requests
import json

def getTechNewsAPI():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c3fc8d32a86f4ab9876325807455e87e"
    r = requests.get(url)
    news = json.loads(r.text)
    articles = news.get("articles", [])
    news_data = [{'title': article.get('title', ''), 'description': article.get('description', ''), 'urlToImage': article.get('urlToImage', ''), 'url': article.get('url', '')} for article in articles]
    return news_data

def getBusinessNewsAPI():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=c3fc8d32a86f4ab9876325807455e87e"
    r = requests.get(url)
    news = json.loads(r.text)
    articles = news.get("articles", [])
    news_data = [{'title': article.get('title', ''), 'description': article.get('description', ''), 'urlToImage': article.get('urlToImage', ''), 'url': article.get('url', '')} for article in articles]
    return news_data

def getbuzzfeedNewsAPI():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=c3fc8d32a86f4ab9876325807455e87e"
    r = requests.get(url)
    news = json.loads(r.text)
    articles = news.get("articles", [])
    news_data = [{'title': article.get('title', ''), 'description': article.get('description', ''), 'urlToImage': article.get('urlToImage', ''), 'url': article.get('url', '')} for article in articles]
    return news_data

def getIndiaEntertainmentNewsAPI():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=c3fc8d32a86f4ab9876325807455e87e"
    r = requests.get(url)
    news = json.loads(r.text)
    articles = news.get("articles", [])
    news_data = [{'title': article.get('title', ''), 'description': article.get('description', ''), 'urlToImage': article.get('urlToImage', ''), 'url': article.get('url', '')} for article in articles]
    return news_data

def getHealthNewsAPI():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=c3fc8d32a86f4ab9876325807455e87e"
    r = requests.get(url)
    news = json.loads(r.text)
    articles = news.get("articles", [])
    news_data = [{'title': article.get('title', ''), 'description': article.get('description', ''), 'urlToImage': article.get('urlToImage', ''), 'url': article.get('url', '')} for article in articles]
    return news_data

def getScienceNewsAPI():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=c3fc8d32a86f4ab9876325807455e87e"
    r = requests.get(url)
    news = json.loads(r.text)
    articles = news.get("articles", [])
    news_data = [{'title': article.get('title', ''), 'description': article.get('description', ''), 'urlToImage': article.get('urlToImage', ''), 'url': article.get('url', '')} for article in articles]
    return news_data

def getWallstreetNewsAPI():
    url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=c3fc8d32a86f4ab9876325807455e87e"
    r = requests.get(url)
    news = json.loads(r.text)
    articles = news.get("articles", [])
    news_data = [{'title': article.get('title', ''), 'description': article.get('description', ''), 'urlToImage': article.get('urlToImage', ''), 'url': article.get('url', '')} for article in articles]
    return news_data

def getArsTechnicaNewsAPI():
    url = "https://newsapi.org/v2/everything?domains=http://arstechnica.com&apiKey=c3fc8d32a86f4ab9876325807455e87e"
    r = requests.get(url)
    news = json.loads(r.text)
    articles = news.get("articles", [])
    news_data = [{'title': article.get('title', ''), 'description': article.get('description', ''), 'urlToImage': article.get('urlToImage', ''), 'url': article.get('url', '')} for article in articles]
    return news_data

def home(request):
    tech_Data = getTechNewsAPI()
    business_Data= getBusinessNewsAPI()
    wallstreet_Data = getWallstreetNewsAPI()
    getBuzzFeed_Data = getbuzzfeedNewsAPI()
    arsTechnical_Data = getArsTechnicaNewsAPI()
    indiaEntertainment_Data = getIndiaEntertainmentNewsAPI()
    health_Data = getHealthNewsAPI()
    science_Data = getScienceNewsAPI()
    return render(request, "petabyte_app/index.html", {'news_data': tech_Data,'business_data': business_Data,'wallstreet_data':wallstreet_Data,'getBuzzFeed':getBuzzFeed_Data, 'arsTechnical':arsTechnical_Data, 'indianEntertainment':indiaEntertainment_Data,'health':health_Data,'science':science_Data})
