from datetime import datetime
import time
import sqlite3
import requests
import selectorlib

url = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

connection = sqlite3.connect("temp.db")


def Data_Scrap(url):
    """Scrape the page source from url"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("scrap_data.yaml")
    value = extractor.extract(source)["temp"]
    return value


def store_data(extracted):
    now = datetime.now().strftime("%y-%m-%d--%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES(?,?)", (now, extracted))
    connection.commit()


if __name__ == "__main__":
    while True:
        data_scrap = Data_Scrap(url)
        extracted = extract(data_scrap)
        print(extracted)
        store_data(extracted)
