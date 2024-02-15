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

skills=['q','w','e','r']

for skill in skills:
    print(f"[Skill {skill.upper()} cool down]")
    try:
        cooldown=driver.find_element(By.CSS_SELECTOR,f'.skill.skill_{skill} div[data-source="cooldown"] .pi-data-value.pi-font')
        print(cooldown.text)
    except:
        try:
            cooldown = driver.find_element(By.CSS_SELECTOR, f'.skill.skill_{skill} div[data-source="static"] .pi-data-value.pi-font')
            print(cooldown.text)
        except:
            try:
                cooldown = driver.find_element(By.CSS_SELECTOR,f'.skill.skill_{skill}qwe div[data-source="cooldown"] .pi-data-value.pi-font')
                print(cooldown.text)
            except:
                print("Dont have cool down")


# exception : Nidalee Elise Jayce Gnar Kled 