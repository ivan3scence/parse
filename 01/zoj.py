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
url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

req = requests.get(url, headers=headers)

src = req.text
# print(src)

with open("soj.html", "w") as file:
    file.write(src)


with open("soj.html") as file:
    src = file.read()
# print(src)
soup = BeautifulSoup(src, "lxml")
# print(soup)

ssilki = soup.find_all(class_="mzr-tc-group-item-href")
dictionary = {}
for x in ssilki:
    x_text = x.text
    x_href = "https://health-diet.ru" + x.get("href")
    dictionary[x_text] = x_href
    # print(x)

with open("dict.json", "w") as file:
    json.dump(dictionary, file, indent=4, ensure_ascii=False)

with open("dict.json") as file:
    dictt = json.load(file)

# print(dictt)

di = {}
for x_name, x_href in dictt.items():
    simvls = [" ", ",", "-", "'"]
    for s in simvls:
        if s in x_name:
            x_name = x_name.replace(s, "_")
    
    req = requests.get(url=x_href, headers=headers)
    req = req.text
    with open(f"data/{x_name}.html", "w") as file_2:
        file_2.write(req)
    
    with open(f"data/{x_name}.html") as file_2:
        src = file_2.read()
    
    soup = BeautifulSoup(src, "lxml")	

    if soup.find(class_="uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed"):
        dishes = soup.find(class_="uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed").find("tbody").find_all("tr")
        # print(dishes)
        for y in dishes:
            k = y.find("a").text
            # print(k)
            di[k] = []
            for i in range(4):
                v = y.find_all(class_="uk-text-right")[i]
                di[k].append(v.text)

with open("di", "w") as file_2:
    file_2.write(str(di))
with open("end/parse.csv", "a", encoding="utf-8") as file_3:
    writer = csv.writer(file_3)
    for key, val in di.items():
        writer.writerow(
            (
                key,
                val[0],
                val[1],
                val[2],
                val[3]
            )
        )
list_di = []
for k, v in di.items():
    list_di.append(
        {
            "Title": k,
            "Calories": v[0],
            "Proteins": v[1],
            "Fats": v[2],
            "Carbohydrates": v[3]
        }
    )
with open("end/parse.json", "a", encoding="utf-8") as file_3:
    json.dump(list_di, file_3, indent=4, ensure_ascii=False)
