import os
import urllib.request
import spider


def save_img(folder, img_list):
    for img_item in img_list:
        img_save = folder + '/' + img_item.split('/')[-1]
        urllib.request.urlretrieve(img_item.replace('\\', ''), img_save)


def down_img(folder, product_list):
    # 单个类别的图片爬取
    img_url = spider.get_img_url(product_list)

    # 获取图片的链接
    img_soup = spider.get_soup(img_url)
    img_list = spider.get_img_list(img_soup)

    # 创建存放文件夹
    if not (os.path.exists(folder)):
        os.mkdir(folder)
        # 将列表的图片链接进行下载存放
        save_img(folder, img_list)
    return
