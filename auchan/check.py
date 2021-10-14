import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from multiprocessing import Pool


# options
# options = webdriver.ChromeOptions()

# # user-agent
# options.add_argument("user-agent=" + "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
# # options.headless = True
# # for ChromeDriver version 79.0.3945.16 or over
# # options.add_argument("--disable-blink-features=AutomationControlled")

# # headless mode
# # options.add_argument("--headless")
# # options.headless = True

# # urls_list = ["https://stackoverflow.com", "https://instagram.com", "https://vk.com"]
# # urls_list = ["Hello", "Ann!"]

# def get_data():
#     try:
#         driver = webdriver.Chrome(
#             executable_path = "/home/ivan/Documentss/parse/amazon/chromedriver",
#             options=options
#         )
#         driver.get("https://www.auchan.ru/")
#         time.sleep(random.randrange(1,120))
#         # login = driver.find_element_by_id("index_email")
#         # login.clear()
#         # login.send_keys("+79158952525")
#         # time.sleep(random.randrange(1,2))
#         # passv = driver.find_element_by_id("index_pass")
#         # passv.clear()
#         # passv.send_keys("Ivan2001Ivan2001")
#         # gal = driver.find_element_by_id("index_expire").click()
#         # time.sleep(random.randrange(1,5))
#         # passv.send_keys(Keys.ENTER)
#         # time.sleep(2)
#         # ann = driver.find_element_by_id("l_fr").click()
#         # time.sleep(2)
#         # massage_ann = driver.find_element_by_class_name("friends_field_act").click()
#         # time.sleep(2)
#         # mas = driver.find_element_by_class_name("mail_box_header_link").click()
#         # time.sleep(2)
#         # masss = driver.find_element_by_id("im_editable115515354")
#         # time.sleep(1)
#         # if s:
#         #     masss.send_keys(s + Keys.ENTER)
#         #     time.sleep(1)

#         # vibor_coobcheniya = driver.find_elements_by_xpath('/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[18]/div[2]')[-1].find_elements_by_xpath('/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[18]/div[2]/ul/li')[-1].click()
#         # time.sleep(1)
#         # urna = driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[4]/button[2]').click()
#         # time.sleep(2)
#         # gal_udalenie_coobcheniya = driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[3]/div[1]/div[2]/div').click()
#         # time.sleep(1)
#         # udalit = driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[3]/div[1]/table/tbody/tr/td[2]/button').click()
#         # time.sleep(1)

#         # logout = driver.find_element_by_class_name("TopNavBtn__profileArrow").click()
#         # time.sleep(1)
#         # log_out = driver.find_element_by_id("top_logout_link").click()
#         # time.sleep(2)

#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.quit()
#         driver.quit()


# if __name__ == '__main__':
#     get_data()
#     p = Pool(processes=2)
#     p.map(get_data, urls_list)

# def get_data(url):
#     try:
#         driver = webdriver.Chrome(
#             executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
#             options=options
#         )
#         # "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
#         # r"C:\users\selenium_python\chromedriver\chromedriver.exe"
#         driver.get(url=url)
#         time.sleep(5)
#         driver.find_element_by_class_name("lazyload-wrapper").find_element_by_class_name("item-video-container").click()
#         time.sleep(random.randrange(3, 10))
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()


# if __name__ == '__main__':
#     process_count = int(input("Enter the number of processes: "))
#     url = input("Enter the URL: ")
#     urls_list = [url] * process_count
#     print(urls_list)
#     p = Pool(processes=process_count)
#     p.map(get_data, urls_list)






from bs4 import BeautifulSoup
import re
import requests
import lxml
import json
import csv

headers = {
    "accept": "*/*", 
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
url = "https://www.auchan.ru/"

req = requests.get(url, headers=headers)

src = req.text
print(src)