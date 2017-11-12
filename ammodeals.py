import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time



# res = requests.get('https://ammoseek.com/go.to/54376990606')
# print(res)
# print(dir(res))
# print(res.text)

def get_deal(ammo):
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://ammoseek.com/ammo/' + ammo)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    # time.sleep(10)
    table = soup.find(string="20 Rd- Wolf Military")
    return table


res = get_deal('223-remington')

print(res)