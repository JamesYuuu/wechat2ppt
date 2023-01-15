import requests
from bs4 import BeautifulSoup
import json

class PictureSpider(object):
    def __init__(self,url):
        self.url=url

    def get_pictures(self):
        link=list()
        r=requests.get(url=self.url)
        soup=BeautifulSoup(r.content,'lxml')
        id=0
        for picture in soup.find_all('img'):
            url=picture.get('data-src')
            width=picture.get('data-w')
            ratio=picture.get('data-ratio')
            if url and width and ratio:
                id=id+1
                link.append({'id':id,'url':url,'width':width,'ratio':ratio})
        return link
