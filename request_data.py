import requests
import re
from bs4 import BeautifulSoup

# 获取唯品会商品页面内容
root = requests.get('https://category.vip.com/')

# 将网页文本写入txt中使用编辑器打开方便查看如何过滤数据
# filename = 'sample.html'
# with open(filename, 'w', encoding='utf-8') as file:
#     file.write(root.text)

# 生成BeautifulSoup对象
# 使用lxml第三方解析器
soup = BeautifulSoup(root.text, "lxml")

# 获取json数据所需tree_id
tree_id = re.search(r'"tree_id":(\d+)', soup.text)

# 获取json数据所需cid
#  中文编码之 .encode('utf-8').decode('unicode_escape')
c_id = re.findall(r'"cate_id":"(\d+)"', soup.text)
# if c_id:
#     for cid in c_id:
#         # 获取json数据url
#         json_url = 'https://category.vip.com/ajax/getTreeList.php?cid={}&tree_id={}'.format(cid[1], tree_id.group(2))
#         print(json_url)

# 测试获取json中的各个小类的url
format_url = 'https://category.vip.com/ajax/getTreeList.php?cid={}&tree_id={}'.format(c_id[0], tree_id.group(1))
req_url = requests.get(format_url)

# filename = 'sample_req.json'
# with open(filename, 'w', encoding='utf-8') as file:
#     file.write(req_url.text)

soup_url = BeautifulSoup(req_url.text, "lxml")

# 找出一二级菜单id对应的名字 用以文件夹命名
cate_dic = re.findall(r'"cate_id":"(\d+)","cate_type":"[12]","cate_name":"([\\u\w+/]+)"', soup_url.text)
name_dic = {}
for item in cate_dic:
    name_dic[item[0]] = item[1].encode('utf-8').decode('unicode_escape')
print(name_dic)

cate = re.findall(r'"cate_id":"(\d+)","cate_type":"(3)","cate_name":"([\\u\w+/]+)","top_cate_id":"(\d+)",'
                  r'"sub_cate_id":"(\d+)",.*?"url":"(.*?)"', soup_url.text)
url_dic = {}
for item in cate:
    for key, value in name_dic.items():
        if item[3] == key:
            name = value
        if item[4] == key:
            name = name+'_'+value
    name = name+'_'+item[2].encode('utf-8').decode('unicode_escape')
    url_dic[name] = item[5]
print(url_dic)


