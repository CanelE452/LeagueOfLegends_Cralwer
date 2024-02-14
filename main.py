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
print("[Skill Q cool down]")
try:
    q=driver.find_element(By.CSS_SELECTOR,'.skill.skill_q div[data-source="cooldown"] .pi-data-value.pi-font')
    print(q.text)
except:
    print("Dont have cool down")

#W
print("[Skill W cool down]")
try:
    w=driver.find_element(By.CSS_SELECTOR,'.skill.skill_w div[data-source="cooldown"] .pi-data-value.pi-font')
    print(w.text)
except:
    print("Dont have cool down")

#E
print("[Skill E cool down]")
try:
    e=driver.find_element(By.CSS_SELECTOR,'.skill.skill_e div[data-source="cooldown"] .pi-data-value.pi-font')
    print(e.text)
except:
    print("Dont have cool down")

#R
print("[Skill R cool down]")
try:
    r=driver.find_element(By.CSS_SELECTOR,'.skill.skill_r div[data-source="cooldown"] .pi-data-value.pi-font')
    print(r.text)
except:
    print("Dont have cool down")