from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def crawling_img(name):
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    #
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    dir = ".\idols" + "\\" + name

    createDirectory(dir) #폴더 생성
    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(3)
            imgUrl = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute(
                "src")
            path = ".\idols\\" + name + "\\"
            urllib.request.urlretrieve(imgUrl, path + name + "_"+ str(count) + ".jpg")

            # 이 아래는 관련이미지 저장
            imgUrl = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[3]/div[3]/c-wiz/div/div/div/div[3]/div[1]/div[1]/a[1]/div[1]/img').get_attribute(
                "src")
            urllib.request.urlretrieve(imgUrl, path + name + "_"+ str(count) + "_1" + ".jpg")
            imgUrl = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[3]/div[3]/c-wiz/div/div/div/div[3]/div[1]/div[2]/a[1]/div[1]/img').get_attribute(
                "src")
            urllib.request.urlretrieve(imgUrl, path + name + "_"+ str(count) + "_2" + ".jpg")

            imgUrl = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[3]/div[3]/c-wiz/div/div/div/div[3]/div[1]/div[3]/a[1]/div[1]/img').get_attribute(
                "src")
            urllib.request.urlretrieve(imgUrl, path + name + "_"+ str(count) + "_3" + ".jpg")
            
            count = count + 1
            if count >= 500:
                break
        except:
            pass
    driver.close()
searching_keyword = ["dinadenoire", "melvnin", "Adut Akech", "lola chuil", "leomie anderson",
"khoudia diop", "zoe saldana", "tyra banks", "karrueche tran", "duckie thot"]

for i in range(len(searching_keyword)) :
    searching_keyword[i] += ' face'

for keyword in searching_keyword:
    crawling_img(keyword)