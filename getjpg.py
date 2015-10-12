# encoding:UTF-8
# import urllib
# import urllib.request
#
# data={}
# data['word']='1'
#
# url_values=urllib.parse.urlencode(data)
# url="http://www.baidu.com/s?"
# full_url=url+url_values
#
# data=urllib.request.urlopen(full_url).read()
# data=data.decode('UTF-8')
# localprint = data.encode('gbk','ignore')
# print(localprint)


# encoding:UTF-8
# import urllib.request
#
# url = "http://tieba.baidu.com/f?kw=lgd&fr=wwwt"
# html = urllib.request.urlopen(url).read()
# data = html.decode('utf-8').encode('gbk', 'ignore')
# # local = data.encode('utf-8')
# name = 'D:/lgd.html'
# with open(name, 'wb') as file:
#     file.write(html)
#     file.close()
# print(data)


# import urllib.request as request
# import urllib.parse as parse
# import string
# print("""
# +++++++++++++++++++++++
#   学校：超神学院
#   专业：德玛班
#   姓名：德玛之力
#   version: python3.2
# +++++++++++++++++=++++
#      """)
# def baidu_tieba(url, begin_page, end_page):
#     for i in range(begin_page, end_page + 1):
#         sName = 'D:/'+str(i).zfill(5)+'.html'
#         print('正在下载第'+str(i)+'个页面, 并保存为'+sName)
#         m = request.urlopen(url+str(i)).read()
#         with open(sName,'wb') as file:
#             file.write(m)
#         file.close()
# if __name__ == "__main__":
#     url = "http://tieba.baidu.com/p/"
#     begin_page = 1
#     end_page = 3
#     baidu_tieba(url, begin_page, end_page)

# import urllib.request as request
# from bs4 import BeautifulSoup
# def taobao(url):
#     response = request.urlopen(url)
#     html = response.read()
#     #我是win7系统，默认是gdk要先解码，再用utf8编码就可以显示汉字了
#     data = html.decode('gbk').encode('utf-8')
#     soup = BeautifulSoup(data)
#     path = 'D:/image/'
#     count = 1
#     for list in soup.find_all('img'):
#         #拆分属性
#         dict = list.attrs
#         if "data-lazy" in dict:
#             image = dict['data-lazy']
#             img = image[image.rfind('.')::]
#             filepath = path + str(count)+img
#             with open(filepath, 'wb') as file:
#                 image_data = request.urlopen(dict['data-lazy']).read()
#                 print(dict['data-lazy'])
#                 file.write(image_data)
#             count += 1
#             file.close()
# if __name__ == '__main__':
#     print("""
# +++++++++++++++++++++++
#   学校：超神学院
#   专业：德玛班
#   姓名：德玛之力
#   version: python3.2
# +++++++++++++++++=++++
#      """)
#     url = 'https://www.taobao.com/'
#     taobao(url)

import urllib.request as request
import re


def getHtml(url):
    page = request.urlopen(url)
    html = page.read().decode('utf-8')
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        request.urlretrieve(imgurl, '%s.jpg' % x)
        print('%s.jpg is download.'%x)
        x += 1


html = getHtml("http://tieba.baidu.com/p/2460150866")

getImg(html)
