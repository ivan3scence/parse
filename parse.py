from bs4 import BeautifulSoup
import re

with open("index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# h1 = soup.find_all("h1")
# print(h1)
# for x in h1:
    # print(x.text)

# userinf = soup.find(class_="user__info").find_all("span")
# print(len(userinf))
# for x in userinf:
#     print(x.string)

# links = soup.find(class_="social__networks").find_all("a")
# print(len(links))
# for x in links:
#     print(x.get("href"))

# parent = soup.find(class_="post__text").find_parent()
# # print(parent)
# print(parent.text)

# siblin = soup.find(class_="user__birth__date").find_all("span")
# for x in siblin:
#     print(x.text)
# print( )
# siblin = soup.find(class_="user__birth__date").find_next_sibling().find_all("span")
# for x in siblin:
#     print(x.text)
# siblin = soup.find(class_="user__birth__date").find_previous_sibling().find_all("span")
# for x in siblin:
#     print(x.text)

# llinks = soup.find(class_="some__links").find_all("a")
# for x in llinks:
#     print(x["href"])
# for x in llinks:
#     print(x.get("data-attr"))

# odejda = soup.find("a", text=re.compile("Одежда"))
# print(odejda.text)

odejda = soup.find_all(text=re.compile("([Оо]дежда)"))
# for x in odejda:
#     print(x.text)
print(odejda)