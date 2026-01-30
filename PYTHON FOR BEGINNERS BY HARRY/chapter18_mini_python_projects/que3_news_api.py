import requests
query = input("What type of news are you interested today? ")
api = "7d9129784d3845bdbb8484a371358deb"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-30&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1,article["title"], article["url"])
    print("\n******************************************************************\n")
    