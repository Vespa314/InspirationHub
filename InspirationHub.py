# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 19:47:26 2015

@author: sherlockye
"""

import re
import sys
pinyin_dict = {}

def LoadPinyinDict():
    global pinyin_dict
    for line in open('pinyin.txt'):
        line = line.replace('\n','')
        line = line.split(":")
        pinyin_dict[unicode(line[0],"utf-8")] = line[1].split(",")

def UniformPinyin(pinyin):
    pinyin, number = re.subn('(.)h(.*)', r'\1\2', pinyin)
    pinyin, number = re.subn('(.*)ng', r'\1n', pinyin)
    return pinyin

def GetPinyin(word):
    if pinyin_dict.has_key(word):
        return pinyin_dict[word][0]
    else:
        return "-"

def convertPinyin(word):
    # word = word.replace(",","")
    return map(lambda x:UniformPinyin(GetPinyin(x)),word)

def ValidCheck(wordList_py,dstWord_py):
    idx = []
    for wordidx,wordpy in enumerate(wordList_py):
        inflag = False
        for pyidx,py in enumerate(wordpy):
            if py in dstWord_py:
                dstidx = dstWord_py.index(py)
                idx.append([wordidx,pyidx,dstidx])
                inflag = True
        if not inflag:
            return []
    return idx

def PrintValidResult(pinyinSet,oriText,wordList):
    line = oriText
    try:
        dstWord_py =  convertPinyin(line)
    except:
        print "Error:%s"%(oriText)
        return
    ReplaceRule = ValidCheck(pinyinSet,dstWord_py)
    if len(ReplaceRule):
        result = list(line)
        for replace_idx in ReplaceRule:
            dst = wordList[replace_idx[0]][replace_idx[1]]
            src = result[replace_idx[2]]
            line = line.replace(src,dst)
        print line,'<<----',oriText

def ReadGushi(filename,pinyinSet,wordList):
    for (linenum,oriText) in enumerate(open(filename)):
        oriText = unicode(oriText.replace('\n',''),"utf-8")
        regexp = "<<(.*)>>:(.*)$"
        result = re.findall(regexp,oriText)
        for (title,poet) in result:
            poet = poet.replace(unicode('，',"utf-8"),'---')
            poet = poet.replace(unicode('。',"utf-8"),'---')
            poet = poet.replace(unicode('？',"utf-8"),'---')
            poet = poet.replace(unicode('、',"utf-8"),'---')
            poet = poet.replace(unicode('！',"utf-8"),'---')
            poet = poet.replace(unicode('；',"utf-8"),'---')
            poet = poet.replace(unicode('：',"utf-8"),'---')
            poet = poet.replace(unicode(':',"utf-8"),'---')
            poet = poet.replace(unicode('”',"utf-8"),'---')
            poet = poet.replace(unicode('“',"utf-8"),'---')
            poet = poet.split('---')
            for p in poet:
                PrintValidResult(pinyinSet,p,wordList)


def main(argv1,argv2):
    wordList = [argv1,argv2]
    wordList = map(lambda x:unicode(x,"utf-8"),wordList)
    pinyinSet = map(lambda x:convertPinyin(x),wordList)
    # ReadGushi("tangshi.txt",pinyinSet,wordList)
    #ReadGushi("songci.txt",pinyinSet,wordList)
    for (linenum,oriText) in enumerate(open('chengyu.txt')):
        oriText = unicode(oriText.replace('\n',''),"utf-8")
        PrintValidResult(pinyinSet,oriText,wordList)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "python InspirationHub.py input1 input2"
    else:
        LoadPinyinDict()
        main(sys.argv[1],sys.argv[2])