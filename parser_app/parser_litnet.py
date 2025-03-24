import requests
from bs4 import BeautifulSoup

URL = "https://litnet.com/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

def get_html(url, params=""):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_data(html):
    bs = BeautifulSoup(html, features="html.parser")
    items = bs.find_all("div", class_="row book-item")
    litnet_list = []
    for item in items:
        title = item.find("h4", class_="book-title").get_text(strip=True)
        litnet_list.append({
            "title": title,
        })
    return litnet_list


def parsing_litnet():
    response = get_html(URL)
    if response.status_code == 200:
        litnet_list2 = []
        for page in range(1, 2):
            response = get_html("https://litnet.com/ru/top/all", params={"page": page})
            litnet_list2.extend(get_data(response.text))
        return litnet_list2
    else:
        raise Exception("error in parsing")

# print(parsing_litnet())






