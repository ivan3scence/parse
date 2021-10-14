from selenium import webdriver
# from selenium.webdriver import Proxy 
import requests
import time

url = "https://www.avito.ru/moskva/kvartiry?cd=1"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + "/home/ivan/.config/google-chrome/Profile 2")
# options.add_argument("Accept-Encoding=gzip, deflate, br")
# options.add_argument("Cache-Control=max-age=0")
# options.add_argument("Connection=keep-alive")
# options.add_argument('Cookie=qrator_jsid=1631832412.808.KwCbsD4cXzL2azZ3-8gbk103o3t8cp9q3r6qlsoqt5170keto; isAddressPopupShown_=true; region_id=1; merchant_ID_=1; methodDelivery_=1; _GASHOP=001_Mitishchi; _gcl_au=1.1.1528632891.1631832415; rrpvid=77015326734664; tmr_lvid=9ae122330f264dd56e431c045c7fd0e5; tmr_lvidTS=1631828312914; _ym_uid=1631828313552655923; _ym_d=1631832416; _gid=GA1.2.236024763.1631832416; _ga_6KC2J1XGF1=GS1.1.1631832415.1.0.1631832415.60; tmr_detect=1%7C1631832415881; rcuid=613de91f660af30001a80bde; _clck=164192l|1|eus|0; mindboxDeviceUUID=983c12aa-82c9-42e2-a3b6-e13d5a9a46c8; directCrm-session=%7B%22deviceGuid%22%3A%22983c12aa-82c9-42e2-a3b6-e13d5a9a46c8%22%7D; _fbp=fb.1.1631832416174.1632863396; _ga=GA1.2.1415793200.1631832416; cto_bundle=C6T7il8lMkJaODNRcGw2YyUyQnFRTDZ0RGNiZVhHTGJXZmYwTiUyQlZLWG5mRTFQYiUyQjglMkI0eEh5Q0JCN05ES2I3bHpWS1NXT0dVVG9pSEJKQiUyRk50OTBWd0tlVXkxdmdkJTJGekI1UEphYzdwU1lEb21STkJxYjBvV2h1dEZGcEdMMUZEMzFqalRib2xrZHZPdG9FTmdnUTFGdmlpZk9EekslMkZnJTNEJTNE; _ym_isad=1; _clsk=aj7ue6|1631832418723|1|1|f.clarity.ms/collect; _dc_gtm_UA-49770337-2=1; tmr_reqNum=55')
# options.add_argument('sec-ch-ua="Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"')
# options.add_argument('sec-ch-ua-platform="Linux"')
# options.add_argument('sec-ch-ua="Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"')
# options.add_argument('Sec-Fetch-Dest=document')
options.add_argument("user-agent=" + "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
# options.add_argument("Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
# options.add_argument("Accept-Language=ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7")
# options.add_argument('--proxy-server=2193.228.49.37:8000')
options.headless = False

# proxy_options = {
#     "proxy": {
#         "https":"http://LGkUVh:RzMJ5m@193.228.49.37:8000"
#     }
# }
try:
    driver = webdriver.Chrome(
        executable_path = "/home/ivan/Documents/drivers_chrome_firefox/chromedriver",
        # seleniumwire_options=proxy_options,
        options=options
    )
    driver.get(url)
    time.sleep(10)
except Exception as ex:
    print("jopa ", ex)
finally:
    driver.quit
    driver.close

###############################################################################################################################################################
# option = webdriver.FirefoxOptions()
# option.set_preference('dom.webdriver.enable', False)
# option.set_preference('dom.webnotifications.enabled', False)
# option.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")

# try:
#     driver = webdriver.Firefox(executable_path='/home/ivan/Documents/drivers_chrome_firefox/geckodriver', options=option)
#     driver.get = ('https://www.auchan.ru/')
#     time.sleep(5)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close
#     driver.quit

# try:
#     driver = webdriver.Firefox(executable_path='/home/ivan/Documents/drivers_chrome_firefox/geckodriver', options=option)
#     driver.get(url="https://www.auchan.ru/")
#     driver.save_screenshot("vk.png")
#     time.sleep(5)
#     time.sleep(2)

#     # driver.get("https://2ip.ru")
#     # time.sleep(5)

# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

