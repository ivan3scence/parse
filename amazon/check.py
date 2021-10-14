import requests
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + "/home/ivan/.config/google-chrome/Profile 2")
options.add_argument("user-agent=" + "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
options.headless = False


def massage(s):
    try:
        driver = webdriver.Chrome(
            executable_path = "/home/ivan/Documentss/parse/amazon/chromedriver",
            options=options
        )
        driver.get("https://vk.com/")
        time.sleep(5)
        login = driver.find_element_by_id("index_email")
        login.clear()
        login.send_keys("+79158952525")
        time.sleep(1)
        passv = driver.find_element_by_id("index_pass")
        passv.clear()
        passv.send_keys("Ivan2001Ivan2001")
        gal = driver.find_element_by_id("index_expire").click()
        time.sleep(1)
        passv.send_keys(Keys.ENTER)
        time.sleep(2)
        ann = driver.find_element_by_id("l_fr").click()
        time.sleep(2)
        massage_ann = driver.find_element_by_class_name("friends_field_act").click()
        time.sleep(2)
        mas = driver.find_element_by_class_name("mail_box_header_link").click()
        time.sleep(2)
        masss = driver.find_element_by_id("im_editable115515354")
        time.sleep(1)
        if s:
            masss.send_keys(s + Keys.ENTER)
            time.sleep(1)

        vibor_coobcheniya = driver.find_elements_by_xpath('/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[18]/div[2]')[-1].find_elements_by_xpath('/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[18]/div[2]/ul/li')[-1].click()
        time.sleep(1)
        urna = driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[4]/button[2]').click()
        time.sleep(2)
        gal_udalenie_coobcheniya = driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[3]/div[1]/div[2]/div').click()
        time.sleep(1)
        udalit = driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[3]/div[1]/table/tbody/tr/td[2]/button').click()
        time.sleep(1)

        logout = driver.find_element_by_class_name("TopNavBtn__profileArrow").click()
        time.sleep(1)
        log_out = driver.find_element_by_id("top_logout_link").click()
        time.sleep(2)

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()
        driver.quit()


mas = "Аня привет?"
mas = mas.split(' ')
if __name__ == '__main__':
    p = Pool(processes=len(mas))
    p.map(massage, mas)
