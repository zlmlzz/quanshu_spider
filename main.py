#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import search, urlmanager, content_downloder, html_parser, outfile

class Main(object):
        

    def __init__(self):
        self.search = search.Search()
        self.urls = urlmanager.UrlManager()
        self.content = content_downloder.ContentDownloder()
        self.parser = html_parser.HtmlParser()
        self.outfile = outfile.OutFile()


    def craw(self, root_url):
        cont = 1
        self.search.get_novel_name()
        books = self.search.search(root_url)
        if books is None:
            return
        for name in books[0]:
            print(name, books[0].index(name) + 1)
        choose_urls = self.search.choose_novel(books)
        self.urls.add_new_url(choose_urls)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            html_content = self.content.downloader(new_url)
            new_urls, new_data = self.parser.parser(new_url, html_content)
            new_urls.sort()
            self.urls.add_new_urls(new_urls)
            self.outfile.collect_data(new_data)
            print(cont)
            cont += 1
#            if cont == 30:
#               break
        self.outfile.output_file()





                



if __name__ == '__main__':
    root_url = 'http://www.quanshuwang.com/modules/article/search.php'
    spider = Main()
    spider.craw(root_url)

        

