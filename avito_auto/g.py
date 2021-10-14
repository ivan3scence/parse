from re import S
from selenium import webdriver
import time
import csv
from PIL import Image
from pytesseract import image_to_string

class Bot:
    def __init__(self):
        self.url_list = []
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.set_preference('dom.webdriver.enable', False)
        options.set_preference('dom.webnotifications.enabled', False)
        options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
        headers = {
            "accept": "*/*", 
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        }
        self.driver = webdriver.Firefox(executable_path='/home/ivan/Documents/drivers_chrome_firefox/geckodriver', options=options)
        # h = 3
        # while h < 12:
        self.driver.get("https://www.avito.ru/kolomna/avtomobili/ford/focus/ii-restayling-20082011_4596-ASgBAgICA0Tgtg2cmCjitg3CpSjqtg3i8ig?p=1&radius=400&s=104&user=1")
        # h += 1
        time.sleep(3)
        sheets =  self.get_sheets()
        self.i = 0 ################################################################################################
        for sheet in sheets:
            # if self.i > 5:
            #     break
            self.tele(sheet)
        ########################## print(self.url_list)
        # self.dick = {}    
        # while self.i > 0:  
        #     telefon = self.tel_recon()
        #     self.dick[f"{self.url_list[self.i - 1]}"] = telefon
        #     self.i -= 1
        # with open("gg", "w") as file:
        #     file.write(str(self.dick))
        # self.csvv()



    def csvv(self, link, telefon):
        with open("avito_ford.csv",'a') as csvfile:
            writer = csv.writer(csvfile)
            # writer.writerow(('Ссылка','Контакт'))
            writer.writerow((link, telefon))
    
    
    # def tel_recon(self):
    #     image = Image.open(f"gifs/{self.i}.gif")
    #     return (image_to_string(image))

        

    def take_screenshot(self):
        self.i += 1
        self.driver.save_screenshot(f"imgs/{self.i}.png")


    def crop(self, location, size):
        image = Image.open(f"imgs/{self.i}.png")
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        image.crop((x, y, x+width, y+height)).save(f"gifs/{self.i}.gif")
        image.close()
        im = Image.open(f"gifs/{self.i}.gif")
        s = image_to_string(im)
        im.close()
        return (s)


    def tele(self, sheet):
        try:
            sheet.click()
            time.sleep(1.5)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(1.5)
            link = self.driver.current_url
            # self.url_list.append(self.driver.current_url)
            print(f"loading: {link}")
            if self.driver.find_element_by_class_name("item-phone-button-sub-text"):
                box = self.driver.find_element_by_xpath('//div[@class="item-phone-number js-item-phone-number greenContact_color "]')
                time.sleep(1)
                box.click()
                time.sleep(2)
            self.take_screenshot()
            image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
            location = image.location
            size = image.size
            telefon = self.crop(location, size)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(1.2)
            self.csvv(link, telefon)
        except Exception as ex:
            print(ex + "def tele")



    def get_sheets(self):
        sheets = self.driver.find_elements_by_xpath("//div[@data-marker='item-photo']")
        time.sleep(1)
        return(sheets)


def main():
    bot = Bot()

if __name__ == "__main__":
    main()