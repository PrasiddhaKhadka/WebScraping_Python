import requests
from bs4 import BeautifulSoup

# soup = BeautifulSoup(open("data/ipl_schedule.html"), "html.parser")
with open("sample.html") as f:
    html_doc = f.read()
    
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title,type(soup.title))
print(soup.div)
# finding all the div tage
print(soup.find_all("div"))

# fing all using for in 
for div in soup.find_all("div"):
    print(div)
    
# finding with id
s = soup.find(id="main-nav")
print(s)

# css selector 
print(soup.select("testing"))

# for parent
for child in soup.find(class_="container").children:
    print(child)


#finding parent from child 
for parent in soup.find(class_="box").parents:
    print(parent)
    # for only single time
    break

# modify the class 
tag = soup.find(class_="box")
tag.name = "boxes"
tag["class"] = "boxes"
print(tag)

# insert new under score tag
# new_tag = soup.new_tag("ul")
# liTag = soup.new_tag("li")
# liTag.string = "This is a new tag"
# liTag 
