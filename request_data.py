import requests
import re
from bs4 import BeautifulSoup

# 获取唯品会网站
root = requests.get('https://www.vip.com/')
# print(root.text)

# 生成BeautifulSoup对象
# 使用lxml第三方解析器
soup = BeautifulSoup(root.text, "lxml")

filename = 'sample.txt'

with open(filename, 'w', encoding='utf-8') as file:
    file.write(root.text)

# main_kind = soup.find_all("a")
# print(main_kind)
