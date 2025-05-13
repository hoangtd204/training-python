import requests
from bs4 import BeautifulSoup

def crawl_title():
    import requests
    from bs4 import BeautifulSoup
    url = 'https://vnexpress.net/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h3', class_='title-news')

        print("📰 Article titles on VnExpress:")
        for title in titles:
            text = title.get_text(strip=True)
            if text:
                print("-", text)
    else:
        print(f"Unable to load the page. Error code: {response.status_code}")

