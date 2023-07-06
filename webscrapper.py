import requests
from bs4 import BeautifulSoup


class WebDataInfo:
    def __init__(self, title, content, links):
        self.title = title
        self.content = content
        self.links = links


web_service = requests.get("https://medium.com")
soup = BeautifulSoup(web_service.content, 'lxml')
base_url = "https://medium.com"

arr_webscrappers = []


totalcontent = soup.find_all("div", class_="pw-homefeed-item")
for data in totalcontent:
    content_tag = data.find("h3", class_="by b eg ca cx ka js jt kb jv jx ik")
    h2_tag = data.find("h2")
    a_tags = data.findAll("a", href=True)
    title = h2_tag.text
    content = content_tag.text
    links = []
    for a_tag in a_tags:
        link = a_tag['href']
        if (link.startswith('/')):
            link = base_url + link
        links.append(link)
    arr_webscrappers.append(WebDataInfo(title, content, links))

print(len(arr_webscrappers))
# print(vars(arr_webscrappers[0]['links']))
print(arr_webscrappers[0].links)
# for obj in arr_webscrappers:
#     print(vars(obj))
