from bs4 import BeautifulSoup
import requests
def Download_data(URL, headers):
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(id="corePrice_desktop").get_text()
    return title, price

