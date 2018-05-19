from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.quora.com/How-would-you-explain-the-central-limit-theorem-in-laymans-terms")
print(page)
print(page.status_code)
print(page.content)
soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify)
list(soup.children)
print(list)
