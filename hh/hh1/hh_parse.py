import requests
import csv
import os
from bs4 import BeautifulSoup
import shutil


headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}
urls_list = []
i = 0
while 1:
    url = f"https://hh.ru/search/vacancy?st=searchVacancy&text=&specialization=23.478&specialization=23.187&specialization=23.479&specialization=23.188&specialization=23.352&specialization=23.476&specialization=23.362&specialization=23.21&specialization=23.477&specialization=23.276&specialization=23.311&specialization=23.29&specialization=23.165&specialization=23.120&specialization=23.759&specialization=23.2&specialization=23.88&industry=29&industry=42&industry=11&industry=27&industry=50&industry=15&industry=46&industry=7&industry=39&industry=33&industry=5&industry=45&industry=24&industry=388&industry=9&industry=52&industry=48&industry=47&industry=389&industry=34&industry=43&industry=41&industry=8&industry=37&industry=13&industry=49&industry=19&industry=44.397&industry=44.395&industry=44.390&industry=44.394&area=2019&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&no_magic=true&L_save_area=true&page={i}"
    
    req = requests.get(url, headers=headers)
    src = req.text
    src = BeautifulSoup(src, "lxml")

    if src.find(class_="error__content"):
        break
    
    if not os.path.exists(".pages"):
        os.mkdir(".pages")
    with open(f".pages/page_{i}.html", "w") as file:
        file.write(req.text)
    
    with open(f".pages/page_{i}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    urls = soup.find_all(class_="resume-search-item__name")
    for x in urls:
        if "https://" in x.find(class_="bloko-link").get("href"):
            urls_list.append(x.find(class_="bloko-link").get("href"))
    i += 1
    if i == 3:
        break


n = 0
listt = []
if not os.path.exists("hhru.csv"):
    with open("hhru.csv", "a", encoding="utf-8") as file_3:
        writer = csv.writer(file_3)
        writer.writerow(
            (
                "Вакансия",
                "Ссылка на вакансию",
                "Компания",
                "Зарплата",
                "Зарплата*",
                "Ссылка на компанию",
                "Описание компании",
                "Собственный сайт компании"
            )
        )
else:
    with open("hhru.csv", "r") as file_3:
        src = csv.reader(file_3)
        for x in src:
            listt.append(''.join(x[1]))

for i in urls_list:
    if i in listt:
        continue
    else:
        print(f"new vacancy's url: {i}")
    req2 = requests.get(i, headers=headers)
    src2 = req2.text
    if not os.path.exists(".urls"):
        os.mkdir(".urls")
    with open(f".urls/url_{n}.html", "w") as file:
        file.write(src2)
    
    with open(f".urls/url_{n}.html") as file:
        src = file.read()
    n += 1
    soup = BeautifulSoup(src, "lxml")
    emploee_name = soup.find_all(class_="bloko-header-1")[1].text
    # print(emploee_name)
    try:
        company_name = soup.find(class_="bloko-header-section-2 bloko-header-section-2_lite").text
    except Exception:
        company_name = ""
    # print(company_name)
    emploee_salary_r = soup.find(class_="vacancy-salary").find("span").text
    # print(emploee_salary_r)
    emploee_salary = ''.join(list(filter(str.isdigit, emploee_salary_r.split(' ')[1])))
    # print(emploee_salary_r, emploee_salary)
    company_url = soup.find(class_="vacancy-company-name").get("href")
    # print(company_url)
    if (company_url):
        company_url = "https://hh.ru" + company_url
        req3 = requests.get(company_url, headers=headers)
        src3 = req3.text
        soup3 = BeautifulSoup(src3, "lxml")
        try:
            company_description = soup3.find(class_="company-description").text
        except Exception:
            company_description = ""
        # print(emploee_name, company_description)
        try:
            company_kontacts = soup3.find(class_="employer-sidebar-content").find("a").get("href")
        except Exception:
            company_kontacts = ""
        if "http" not in company_kontacts:
            company_kontacts = ""
        # print(emploee_name, company_name, company_kontacts)
    
    with open("hhru.csv", "a", encoding="utf-8") as file_3:
        writer = csv.writer(file_3)
        writer.writerow(
            (
                emploee_name,
                i,
                company_name,
                emploee_salary_r,
                emploee_salary,
                company_url,
                company_description,
                company_kontacts
            )
        )

shutil.rmtree(".pages")
shutil.rmtree(".urls")