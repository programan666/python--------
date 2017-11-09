
'''
Created on Oct 17, 2017

@author: Administrator
'''
import requests
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
#tieba.baidu.com/f/search/res?isnew=1&kw=&qw=ps%BD%CC%B3%CC%20%D3%CA%CF%E4&rn=10&un=&only_thread=0&sm=1&sd=&ed=&pn=2
def getArticleList(pn=1):
    response = requests.get('http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=ps%BD%CC%B3%CC%20%D3%CA%CF%E4&rn=10&un=&only_thread=0&sm=1&sd=&ed=&pn={}'.format(pn),headers=headers)
    html = response.text
    reg = r'"(/p/\d+\?pid=\d+&cid=\d+#\d+)"'
    return re.findall(reg, html)

def getArticleContent(url):
    html = requests.get('https://tieba.baidu.com{}'.format(url),headers=headers).text
    reg = r'[0-9a-zA-Z-_\.]+@[0-9a-zA-z-_\.]+\.[a-zA-z]+'
    mailList = re.findall(reg,html)
    print(mailList)
    fn = open('F:\python\email.txt','a')
    for mail in mailList:
        fn.write('{}\n'.format(mail))
    fn.close()
    reg = r'<a href="(.*?)下一页</a>">'
    next = re.findall(reg,html)
    if not next:
        print('已经是最后一页')
        return
    print('正在爬取下一页')
    getArticleContent(next[0])

for pn in range(1,77):
    for articleUrl in getArticleList(pn):
        print(articleUrl)
        getArticleContent(articleUrl)
   
files = open('email.txt').readlines()
files = set(files)

with open('F:\python\email.txt','w') as fn:
    for i in files:
        fn.write(i)
   
print('搞定')
    