from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")


time.sleep(2)
html=driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[1]/td[1]/span/span/a/text()[0]')



print(html)














# response = requests.get(url)
# soup = BeautifulSoup(response.content,'html.parser')
# html=soup.find_all("span",class_="inline-image label-only")
# print(html)
