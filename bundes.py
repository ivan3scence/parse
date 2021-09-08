from bs4 import BeautifulSoup
import requests
import json

def cut(str):
    sep = [' ', ',', "'", '-', '.', '(', ')']
    for s in sep:
        if s in str:
            str = str.replace(s, '_')
    return(str)

url = "https://www.bundestag.de/ajax/filterlist/en/members/453158-453158?limit=9999&view=BTBiographyList"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
req = requests.get(url, headers=headers)
src = req.text
# print (src)

with open("temp/bundes.html", "w") as file:
    file.write(src)

with open("temp/bundes.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

members = soup.find_all("li")
# print(members)
# members_links = []
# for x in members:
#     members_links.append(x.find("a").get("href"))
# print(members_links)

for member in members:
    with open(f"data/{cut(member.find('h3').text)}.html", "w", encoding="utf-8") as file:
        file.write(requests.get(member.find("a").get("href")).text)
# k = 0
listt = []
for member in members:
    # if k == 2:
    #     break
    # k += 1
    with open(f"data/{cut(member.find('h3').text)}.html") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    # print(soup)

    member_dict = {}

    try:
        soup1 = soup.find(class_="bt-profil row")
        member_name = soup1.find(class_="col-xs-8 col-md-9 bt-biografie-name").text.split(',')[0].split()
        member_name = " ".join(member_name)
        # print(member_name)
    except Exception:
        member_name = "no name"

    try:
        member_job = soup1.find(class_="col-xs-8 col-md-9 bt-biografie-name").text.split(',')[1].split('\n')[0][1:]
        # print(member_job)
    except Exception:
        member_job = "no company"

    # member_job_position = soup1.find(class_="col-xs-8 col-md-9 bt-biografie-name").text.split('\n')[-3]
    # print(member_job_position)

    try:
        member_links_soup = soup.find(class_="col-xs-12 col-md-4").find_all("li")
        # print(member_links_soup)
        member_links = []
        for link in member_links_soup:
            member_links.append(link.find("a").get("href"))
        # print(member_links)
    except Exception:
        member_links = "no links"

    listt.append(
        {
            "Member name": member_name,
            "Member company": member_job,
            "Member links": member_links,
        }
    )

with open("end/members.json", "w", encoding="utf-8") as file:
    json.dump(listt, file, indent=4, ensure_ascii=False)