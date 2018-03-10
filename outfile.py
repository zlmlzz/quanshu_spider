#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class OutFile(object):

    def __init__(self):
        self.datas = []
        
    def collect_data(self, data):
        if data is None:
            return 
        self.datas.append(data)


    def output_file(self):
        with open('out.txt', 'a') as f:
            for data in self.datas:
                try:
                    f.write('\n' + data['title'] + '\n')
                    f.write('    ' + data['content'])
                except:
                    pass
