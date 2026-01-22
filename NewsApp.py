#News API=Search worldwide news with code.A News API lets your code ask questions like:“Give me today’s tech news”,“Show headlines about AI”,“Fetch business news from India.
#Exercise=Use the NewsAPI and the requests module to fetch the daily news related to different topics.Go to:https://newsapi.org/ and explore the various options to build you application.

import requests

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(topic, page_size=5):
    params = {
        "q": topic,
        "language": "en",
        "pageSize": page_size,
        "apiKey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return

    data = response.json()

    for i, article in enumerate(data["articles"], start=1):
        print(f"\n{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   URL: {article['url']}")
topics = ["AI", "Sports", "Technology", "Finance"]

for topic in topics:
    print(f"\n===== News about {topic} =====")
    fetch_news(topic)

