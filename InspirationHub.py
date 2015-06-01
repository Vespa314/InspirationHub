# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 19:47:26 2015

@author: sherlockye
"""

pinyin_dict = {}

def LoadPinyinDict():
    global pinyin_dict
    for line in open('pinyin.txt'):
        line = line.split(":")
        pinyin_dict[line[0]] = line[1].split(",")

if __name__ == "__main__":
    LoadPinyinDict()
    print 'pinyin dict load Finished!'
    
