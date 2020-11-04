from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import etree
import re

chrome_driver = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/selenium/chromedriver'

def cpture(url, i):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
    driver.maximize_window()
    driver.get(url)

    html = driver.page_source
    content = etree.HTML(html)
    title = content.xpath("//div[@class='rich_media_area_primary_inner']/div[@id='img-content']/h2[@id='activity-name']/text()")
    ptime = content.xpath("//div[@class='rich_media_area_primary_inner']/div[@id='img-content']/div[@id='meta_content']/em[@id='publish_time']/text()")
    
    if len(ptime) != 0:
        ptime = re.sub(r'(\s+)', '', ptime[0])
        ptime = re.sub(r'/', '_', ptime)
    else:
        ptime = ''

    if len(title) != 0:
        picname = re.sub(r'(\s+)', '', title[0]) + '  ' + ptime
    else:
        picname = str(i)
    js_height = "return document.body.clientHeight"

    try:
        driver.get(url)
        k = 1
        height = driver.execute_script(js_height)
        while True:
            if k * 500 < height:
                js_move = "window.scrollTo(0,{})".format(k * 500)
                print(js_move)
                driver.execute_script(js_move)
                time.sleep(0.5)
                height = driver.execute_script(js_height)
                k += 1
            else:
                break
        scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        
        '''
        STR_READY_STATE = ''
        time_start = time.time()

        while STR_READY_STATE != 'complete':
             time.sleep(0.1)
             STR_READY_STATE = driver.execute_script('return document.readyState')
             time_end = time.time()
             if int(time_end - time_start) > 60:
                break
        if STR_READY_STATE == 'complete':
            driver.set_window_size(scroll_width, scroll_height)
            print(picname, '   ', i)
            driver.get_screenshot_as_file("./pic/" + picname + ".png")
        else:
            print('*********error for {}*********'.format(i))
        '''

        '''
        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html//section/img'))
            )
            driver.set_window_size(scroll_width, scroll_height)
            print(picname, '   ', i)
            driver.get_screenshot_as_file("./pic/" + picname + ".png")
        except:
            print('*********error for {}*********'.format(i))
        '''
        time.sleep(1)
        driver.set_window_size(scroll_width, scroll_height)
        print(picname, '   ', i)
        driver.get_screenshot_as_file("./pic/" + picname + ".png")

    except Exception as e:
        print(picname, e)

    driver.close()


with open('t.txt', 'r') as f:
    tlist = f.read().split()
for i in range(53, len(tlist)):
    cpture(tlist[i], i)



