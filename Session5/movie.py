from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains
import bs4
from bs4 import BeautifulSoup
import requests


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'C:/Users/hanbyul.kim/Desktop/NEXT_HW/Session5/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

driver.get("https://movie.naver.com")
action=ActionChains(driver)

file=open('movie.csv', mode='w', newline='')
writer=csv.writer(file)
writer.writerow(["title", "genre", "director"])

##1~20위
# btn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
# btn.click()

# res=driver.page_source
# soup=BeautifulSoup(res, "html.parser")

# for i in range(2, 23):
#     element=soup.select_one(f"#old_content > table > tbody > tr:nth-child({i}) > td.title > div > a")
#     if element is not None:
#         print(element.text)


#1~20위 정보
btn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
btn.click()
res1=driver.page_source
soup1=BeautifulSoup(res1, "html.parser")

for i in range(2, 23):
  element=soup1.select_one(f"#old_content > table > tbody > tr:nth-child({i}) > td.title > div > a")

  if element is not None:
    title=element.text
    btn = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a')
    btn.click()
    res2=driver.page_source
    soup2=BeautifulSoup(res2, "html.parser")
    genre=soup2.select_one("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a").text
    director=soup2.select_one("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a").text
    print(title, genre, director)
    writer.writerow([title, genre, director])
    driver.back()
file.close


##좋아하는 영화 검색
# btn = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
# btn.click()
# ActionChains(driver).send_keys('대외비').perform()
# btn = driver.find_element(By.XPATH, '//*[@id="jSearchArea"]/div/button')
# btn.click()
# btn = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li/dl/dt/a/strong')
# btn.click()

# res1=driver.page_source
# soup1=BeautifulSoup(res1, "html.parser")
# title=soup1.select_one("#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)").text
# director=soup1.select_one("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a").text

# section = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]')
# action.move_to_element(section).perform()
# res2=driver.page_source
# soup2=BeautifulSoup(res2, "html.parser")
# rate=soup2.select_one("#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_area > div.netizen_score > div > div > em").text
# num=soup2.select_one("#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_total > strong > em").text

# print(title, director, rate, num)