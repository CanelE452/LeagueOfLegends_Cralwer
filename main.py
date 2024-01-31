from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

url="https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki"

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
print(soup.find_all("span",class_="grid-icon"))