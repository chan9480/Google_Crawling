import sys
import shutil
import os
import requests
from selenium import webdriver
from selenium.webdriver.safari.options import Options
import datetime
import time

def get_src(element):
    return element.get_attribute('src')



def doScrollDown(driver, whileSeconds):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=whileSeconds)
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)
        if datetime.datetime.now() > end:
            break


def crawling(url, n):
    # 같은 위치에 imgs라는 폴더 생성(초기화)
    # imgs 폴더에, n개의 이미지 저장
    if os.path.exists('./imgs') :
        shutil.rmtree('./imgs')
    os.mkdir('./imgs')

    with webdriver.Safari() as driver:
        option = Options()
        driver.set_window_size(1600, 2000)
        driver.get(url)

        doScrollDown(driver, 300)
        driver.implicitly_wait(1000)

        class_name  =  driver.find_elements_by_class_name("Image--image")
        class_name = list(map(get_src , class_name))

    print('다운받을 수 있는 갯수', len(class_name))
    print('요청받은 다운 갯수', n)

    num = min(len(class_name), n)
    print('다운받을 갯수', num)
    print('첫번쨰이미지url', class_name[0])
    for i in range(num):
        img_url = class_name[i]
        image_name = './imgs/'+str(i)+'.png'
        try :
            icon_requests = requests.get(img_url)
            with open(image_name, 'wb') as icon:
                icon.write(icon_requests.content)
        except:
            print('requests 오류')




if __name__ == '__main__':
    url = sys.argv[1]
    n = int(sys.argv[2])
    crawling(url, n)
