#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, time, random


class ContentDownloder(object):
    def __init__(self):
       self.headers = {
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate',
               'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.132 Chrome/63.0.3239.132 Safari/537.36'

       }
        

    def downloader(self, url, try_times=3):
        if url is None:
            return None
        time.sleep(random.random() * 0.5)
        try:
            response = requests.get(url, headers=self.headers, timeout=5)
        except:
            if try_times > 0:
                return self.downloader(url, try_times-1)
            print(url + 'failed')
        response.encoding = 'gbk'
        return response.text
