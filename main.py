from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.leagueoflegends.com/en-us/champions/")

driver.implicitly_wait(2)

chms=driver.find_elements(By.CSS_SELECTOR,".style__Text-sc-n3ovyt-3.kThhiV")

champions=[]

for chm in chms:
    champions.append(chm.text)

print("[List of champions]")
num=1
for chm in champions:
    print(f"{num} - {chm}")
    num+=1

choose=int(input("Choose a champion number : "))
print(f"You have chosen {champions[choose-1]}")

# 데이터 가공
for idx in range(len(champions)):
    chm = champions[idx].lower()
    champions[idx] = chm
    if "&" in chm:
        champions[idx]=chm[:chm.find("&")]



#데이터 검색
driver.get(f"https://leagueoflegends.fandom.com/wiki/{champions[choose-1]}/LoL")
driver.implicitly_wait(2)

#Q
q=driver.find_elements(By.CSS_SELECTOR,'div[data-source="cooldown"] .pi-data-value.pi-font')[0]
print("[Skill Q cool down]")
print(q.text)

#W
w=driver.find_elements(By.CSS_SELECTOR,'div[data-source="cooldown"] .pi-data-value.pi-font')[1]
print("[Skill W cool down]")
print(w.text)

#E
e=driver.find_elements(By.CSS_SELECTOR,'div[data-source="cooldown"] .pi-data-value.pi-font')[2]
print("[Skill E cool down]")
print(e.text)

#R
r=driver.find_elements(By.CSS_SELECTOR,'div[data-source="cooldown"] .pi-data-value.pi-font')[3]
print("[Skill R cool down]")
print(r.text)







