from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Users\\Mirrovex_PC\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://play.aidungeon.io/main/scenarioPlay?publicId=756f8cd0-6349-11ec-b65a-a9045c21f45d")


#search = WebDriverWait(driver, 10).until(driver.find_element(By.ID, "root"))
wait = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class='css-901oao r-1loqt21 r-1xnzce8 r-13qz1uu']"
    ))
).text
select = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-16y2uox']")
styl = select.find_elements(By.XPATH, ".//div[@class='css-901oao r-1loqt21 r-1xnzce8 r-13qz1uu']") #wybiera wszystkie divy z selecta
#for el in styl: #wyswietla wszystkie teksty divov ze stylu
    #print(el.text)
print(styl[1].text)
styl[1].click() #klika wybrana opcje

time.sleep(1)

wait = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class='css-901oao r-1loqt21 r-1xnzce8 r-13qz1uu']"
    ))
).text
select = driver.find_elements(By.XPATH, "//div[@class='css-1dbjc4n r-16y2uox']")[2]
postac = select.find_elements(By.XPATH, ".//div[@class='css-901oao r-1loqt21 r-1xnzce8 r-13qz1uu']") #wybiera wszystkie divy z selecta
print(postac[1].text)
postac[1].click()

time.sleep(1)

wait = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class='css-901oao r-1loqt21 r-1xnzce8 r-13qz1uu']"
    ))
).text
#select = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1777fci r-13qz1uu']")
imie = driver.find_elements(By.XPATH, ".//textarea[@class='css-11aywtz r-13awgt0 r-1777fci r-snp9zz']")[2] #wybiera wszystkie divy z selecta
imie.send_keys('Imie')
imie.send_keys(Keys.RETURN)





#search = driver.find_element(By.XPATH, "//textarea[@class='css-11aywtz r-13awgt0 r-1777fci r-snp9zz']")
#search.send_keys('1')
#search.send_keys(Keys.RETURN)

"""search = driver.find_element(By.CLASS_NAME, "css-11aywtz r-13awgt0 r-1777fci r-snp9zz")
search.send_keys('1')
search.send_keys(Keys.RETURN)"""

time.sleep(5)

#driver.quit()
