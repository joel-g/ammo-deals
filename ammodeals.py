import requests
from selenium import webdriver
from bs4 import BeautifulSoup



# res = requests.get('https://ammoseek.com/go.to/54376990606')
# print(res)
# print(dir(res))
# print(res.text)

def get_deal(ammo):
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://ammoseek.com/ammo/' + ammo)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="main").find("table")
    return table


print(get_deal('223-remington'))