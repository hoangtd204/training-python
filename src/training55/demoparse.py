import requests
from bs4 import BeautifulSoup


def get_inf():
    url = "https://apidog.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    print("All the links on the page:")
    for link in links:
        href = link.get("href")
        if href:
            print(url + href if href.startswith("/") else href)
