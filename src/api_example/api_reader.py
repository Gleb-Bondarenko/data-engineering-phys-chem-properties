import requests
import pandas as pd
import os
from io import BytesIO
from PIL import Image
import json
# NASA OPEN API - Astronomy Picture of the Day #

API_KEY = "DEMO_KEY"
API_URL = "https://api.nasa.gov/planetary/apod"


def fetch_apod(api_key=API_KEY, date=None):
    params = {"api_key": api_key}
    if date:
        params["date"] = date 
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()


def apod_to_dataframe(apod_json):
    df = pd.DataFrame([{
        "date": apod_json.get("date"),
        "title": apod_json.get("title"),
        "media_type": apod_json.get("media_type"),
        "url": apod_json.get("url"),
        "hdurl": apod_json.get("hdurl"),
        "explanation": apod_json.get("explanation"),
    }])
    return df

# Моя любимая часть :)

def show_image_from_url(url):
    print("Загружаю и открываю изображение...")
    response = requests.get(url)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    img.show()  # откроет фото системной программой


def main():
    cache_filename = "apod_cached.json"
    if os.path.exists(cache_filename):
        with open(cache_filename, "r") as f:
            apod_json = json.load(f)
    else:
        print("Запрашиваю у NASA API")
        apod_json = fetch_apod()
        # сохранить локально
        with open(cache_filename, "w") as f:
            json.dump(apod_json, f, indent=2)

    df = apod_to_dataframe(apod_json)
    print(df)

    df.to_csv("apod_data.csv", index=False)

 # показать изображение, если это картинка
    if apod_json.get("media_type") == "image":
        show_image_from_url(apod_json.get("url"))
    else:
        print("Сегодняшний APOD не изображение (например, видео).")
if __name__ == "__main__":
    main()
