import requests
from bs4 import BeautifulSoup


class WebDataInfo:
    def __init__(self, title, content, link):
        self.title = title
        self.content = content
        self.link = link


web_service = requests.get("https://medium.com")
soup = BeautifulSoup(web_service.content, 'lxml')
base_url = "https://medium.com"

arr_webscrappers = []


totalcontent = soup.find_all("div", class_="al db")
print(totalcontent)
# for data in totalcontent:
#     content_tag = data.find("h3")
#     h2_tag = data.find("h2")
#     link_tag = data.findAll("a", href=True)
#     title = h2_tag.text
#     content = content_tag.text
#     links = []
#     for link in link_tag:
#         links.append(link['href'])
#     arr_webscrappers.append(WebDataInfo(title, content, links))


print(arr_webscrappers)
# for obj in arr_webscrappers:
#     print(vars(obj))
