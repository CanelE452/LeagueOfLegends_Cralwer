from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.leagueoflegends.com/en-us/champions/")

driver.implicitly_wait(2)

# htmls=driver.find_elements(By.CSS_SELECTOR,".style__Text-sc-n3ovyt-3 .")
chms=driver.find_elements(By.CSS_SELECTOR,".style__Text-sc-n3ovyt-3.kThhiV")

champions=[]

for chm in chms:
    champions.append(chm.text)

print(champions)














# response = requests.get(url)
# soup = BeautifulSoup(response.content,'html.parser')
# html=soup.find_all("span",class_="inline-image label-only")
# print(html)
