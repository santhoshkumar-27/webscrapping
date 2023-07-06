import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SmartWork_1234",
    database="webscrapping"
)
mycursor = mydb.cursor()
base_url = "https://medium.com"
arr_webscrappers = []


class WebDataInfo:
    def __init__(self, title, content, links, imgUrl):
        self.title = title
        self.content = content
        self.links = links
        self.imageLink = imgUrl


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://medium.com")
time.sleep(1)
elem = driver.find_element(By.TAG_NAME, "body")
no_of_pagedowns = 25
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    no_of_pagedowns -= 1

post_elems = driver.find_elements(By.CLASS_NAME, "pw-homefeed-item")
for post in post_elems:
    title = post.find_element(By.TAG_NAME, 'h2').text
    contents = post.find_elements(By.TAG_NAME, 'h3')
    for cont in contents:
        content = cont.text
    elems = post.find_elements(By.TAG_NAME, 'a')
    imgUrls = post.find_elements(By.TAG_NAME, 'img')
    imgUrl = ''
    for url in imgUrls:
        if (url.get_attribute('alt') == title):
            imgUrl = url.get_attribute('src')
            break

    linksElementCollection = [elem.get_attribute('href') for elem in elems]
    links = []
    for link in linksElementCollection:
        if (link.startswith('/')):
            link = base_url + link
        links.append(link)
    arr_webscrappers.append(WebDataInfo(title, content, links, imgUrl))

for obj in arr_webscrappers:
    sql = "INSERT INTO medium_site (title, content, links, imgLink) VALUES (%s, %s, %s, %s)"
    val = (obj.title, obj.content, json.dumps(obj.links), imgUrl)
    mycursor.execute(sql, val)
print(len(arr_webscrappers))

mydb.commit()
