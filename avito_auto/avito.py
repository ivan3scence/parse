from bs4 import BeautifulSoup
import os.path
import requests
from selenium import webdriver
import time
import csv
from PIL import Image
import lxml
from pytesseract import image_to_string
from table import tablee

class Bot:
    def __init__(self):
        headers = {
            "accept": "*/*", 
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        }
        i = 1
        self.table = tablee
        # while i < 16:
        #     avtoru = requests.get("https://auto.ru/kolomna/cars/ford/focus/2306579/all/?has_image=false&seller_group=PRIVATE&page={i}", headers=headers)
        #     i = i + 1
        #     src = avtoru.text
        #     soup = BeautifulSoup(src, "lxml")
        #     self.get_sheets(soup)
        # with open("table.py", "w") as file:
        #     file.write(str(self.table))
        print(len(self.table))
        urls = self.check_csv()
        for x in self.table:
            if x in urls:
                continue
            self.get_tele(x)


    def check_csv(self):
        urls = []
        if os.path.exists('avtoru.csv'):
            with open("avtoru.csv", "r") as file:
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    urls.append(row[0])
        return(urls)


    def get_tele(self, url):
        try:
            print(f"loading:...{url}")
            # options = webdriver.ChromeOptions()
            # options.add_argument("user-agent=" + "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
            # options.headless = True
            # driver = webdriver.Chrome(
            #     executable_path = "/home/ivan/Documents/drivers_chrome_firefox/chromedriver",
            #     options=options
            # )
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            options.set_preference('dom.webdriver.enable', False)
            options.set_preference('dom.webnotifications.enabled', False)
            options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
            driver = webdriver.Firefox(executable_path='/home/ivan/Documents/drivers_chrome_firefox/geckodriver', options=options)
            driver.get(url)
            
            # if not driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/button"):
            time.sleep(5)
            print("...")
            tele_box = driver.find_element_by_class_name("Button Button_color_green Button_size_l Button_type_button Button_width_full Button_radius_r8 OfferPhone CardOwner__phone OfferPhone_button").click()
            # if not driver.find_element_by_class_name("SellerPopup__phoneNumber"):
            time.sleep(5)
            print("...")
            telefon = str(driver.find_element_by_class_name("SellerPopup__phoneNumber").text)
            print(telefon)
            listt = []
            listt.append(url)
            listt.append(telefon)
            self.csvv(listt)
        except Exception as ex:
            print(ex + "gg")
            print(url)
        finally:
            driver.close()
            driver.quit()


    def csvv(self, listt):
        with open("avtoru.csv",'a') as csvfile:
            writer = csv.writer(csvfile)
            # writer.writerow(('Ссылка','Контакт'))
            writer.writerow(listt)


    def get_sheets(self, soup):
        sheets = soup.find_all(class_="ListingItem")
        for sheet in sheets:
            x = sheet.find(class_="Link OfferThumb").get("href")
            self.table.append(x)
        return(self.table)


def main():
    bot = Bot()

if __name__ == "__main__":
    main()
        
