import requests
from bs4 import BeautifulSoup
import pandas as pd

# Загружаем HTML страницу
URL = "https://quotes.toscrape.com"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

# Извлекаем нужные данные
data = []
for q in quotes:
    text = q.find("span", class_="text").get_text(strip=True)
    author = q.find("small", class_="author").get_text(strip=True)
    tags = [t.get_text(strip=True) for t in q.find_all("a", class_="tag")]
    data.append({"text": text, "author": author, "tags": ", ".join(tags)})

# Сохраняем в DataFrame
df = pd.DataFrame(data)
print(df.head())

# Сохраняем для проверки
df.to_csv("quotes.csv", index=False)