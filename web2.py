import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()

browser.get("https://medium.com")
time.sleep(1)
elem = browser.find_element(By.TAG_NAME, "body")
# myLink = browser.find_element(By.CLASS_NAME, 'mm')
# myLink.click()
no_of_pagedowns = 20
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    # myLink.click()
    # Find the parent element
    parent_element = browser.find_element(By.CLASS_NAME, "mm")

    child_element = WebDriverWait(parent_element, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )
    # Find the child element within the parent element
    # child_element = parent_element.find_element(By.TAG_NAME, "button")

    # Click on the child element
    child_element.click()
    time.sleep(1)
    no_of_pagedowns -= 1


post_elems = browser.find_element(By.CLASS_NAME, "pw-homefeed-item")
print(post_elems)
# for post in post_elems:
#     print(post.text)
