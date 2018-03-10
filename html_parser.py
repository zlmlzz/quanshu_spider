#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re


class HtmlParser(object):
        

        def parser(self, page_url, html_cont):
            if page_url is None or html_cont is None:
                return 

            soup = BeautifulSoup(html_cont, 'html.parser')
            new_urls = self._get_new_urls(page_url, soup)
            new_data = self._get_new_data(page_url, soup)
            return new_urls, new_data


        def _get_new_urls(self, page_url, soup):
                new_urls = set()
                links = soup.find_all('a',href=re.compile(r'http://www.quanshuwang.com/book/\d+/\d+/\d+\.html'), title=re.compile(r'\w+'))
                for link in links:
                        new_url = link['href']
                        new_urls.add(new_url)

                return list(new_urls)

        def _get_new_data(self, page_url, soup):
                res_data = {}
                try:
                    title_node = soup.find('title')
                    res_data['title'] = title_node.string.split('_')[1]
                    print(res_data['title'])
                    content_node = soup.find('div', class_='mainContenr')
                    res_data['content'] = ''.join(content_node.get_text().split())
                except:
                    print(page_url, '此页面没有内容')
                return res_data



                
            
