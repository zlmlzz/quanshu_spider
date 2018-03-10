#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from content_downloder import ContentDownloder
from bs4 import BeautifulSoup
from urllib.request import quote, unquote
import requests, time, re


class Search(object):
    

    def __init__(self):
       self.headers = {
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate',
               'Accept-Language':'zh-CN,zh;q=0.9',
               'Connection':'keep-alive',
               'Host':'www.quanshuwang.com',
               'Referer':'http://www.quanshuwang.com/',
               'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.132 Chrome/63.0.3239.132 Safari/537.36'
       }
       self.downloder = ContentDownloder()
       self.books_name = []
       self.books_url = []
       self.allbooks = [self.books_name, self.books_url]

       self.novel_name = self.get_novel_name()
       self.payload = {
        'searchkey':self.novel_name,
        'searchtype':'articlename',
        'searchbuttom.x':0,
        'searchbuttom.y':0,
       }
    

    def get_novel_name(self):
        novel_name = input('enter your novel:')       
        if novel_name is None:
            return
        return novel_name.encode('gbk')

    def search(self, root_url):
        if root_url is None:
            return
        response = requests.get(root_url, headers=self.headers, params=self.payload, timeout=30)
        time.sleep(1)
        response.encoding = 'gbk'
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        start_url = soup.find('a', class_='reader')
        if start_url is not None:
            self.books_name.append(start_url['title'])
            self.books_url.append(response.url)
        else:
            print('没有你想要的书')
            return
        books = soup.find_all('a',target='_blank', href=re.compile(r'http://www.quanshuwang.com/book_\d+\.html'))
        for book in books:
            if book.string is None:
                continue
            self.books_name.append(book.string)
            self.books_url.append(book['href'])
        page_urls = soup.find('a', class_='next')
        if page_urls is None:
            if self.allbooks is None or len(self.allbooks) == 0:
                print('没有你想要的书')
            return self.allbooks
        else:
            page_url = 'http://www.quanshuwang.com' + page_urls['href']
            return self.search(page_url)


    def choose_novel(self, books, num=1):
        if books is None or len(books) == 0:
            return
        number = int(input('choose one:'))
        if 0 < number <= len(books[0]):
            
            start_html = self.downloder.downloader(url=books[1][number - 1])
            start_soup = BeautifulSoup(start_html, 'html.parser')
            start_url = start_soup.find('a', class_='reader')
            return start_url['href']
        else:
            print('Invalid number')
            if num > 0:
                return self.choose_novel(books, num - 1)
            else:
                print('game over')
                return
            
