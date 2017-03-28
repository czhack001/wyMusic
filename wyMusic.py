#!/usr/bin/env python
#-*- coding:utf-8 -*-
# http://www.0day.me
#船长哥哥
import urllib
import json
import StringIO
import gzip
import os
import re
import time
# songID=''
# url='http://music.163.com/api/song/detail/?id='+songID+'&ids=%5B'+songID+'%5D'
# print url
def optMan():
    s=raw_input("单曲下载输入1，歌单下载输入2:")
    if s=='1':
        s1=raw_input("单曲ID下载输入1，分享地址下载输入2:")
        if s1=='1':
            id=raw_input("请输入ID号码:")
            id1=songUrl(id)
            down(id1)
        else:
            url1=raw_input("请输入分享网址:")
            id2=muUrl(url1)
            down(id2)
    elif s=='2':
        s1=raw_input("歌单ID下载输入1，分享地址下载输入2:")
        if s1=='1':
            id=raw_input("请输入ID号码:")
            id1=muList(id)
            songList(id1)
        else:
            url1=raw_input("请输入网址:")
            id2=listUrl(url1)
            songList(id2)
def muList(songID):#ID就能下载
    url='http://music.163.com/api/playlist/detail?id='+songID+'&updateTime=-1'
    return url
def listUrl(urlid):#需要输入网址
    reid='id=(.*)&'
    s=re.findall(reid,urlid)
    url='http://music.163.com/api/playlist/detail?id='+s[0]+'&updateTime=-1'
    return url
def songUrl(songID):
    url='http://music.163.com/api/song/detail/?id='+songID+'&ids=%5B'+songID+'%5D'
    return url
def muUrl(urlid):
    reid='id=(.*)&'
    s=re.findall(reid,urlid)
    url='http://music.163.com/api/song/detail/?id='+s[0]+'&ids=%5B'+s[0]+'%5D'
    return url
def songList(url):#网易云列表
    num=0
    resp=urllib.urlopen(url).read()
    try:
        buf=StringIO(resp)
        f=gzip.GzipFile(fileobj=buf)
        data=f.read()
    except:
        data=resp
    result=json.loads(data)
#    print result.get('result')['trackCount']
    dir = r'd:\music'
    try:
        while num<result.get('result')['trackCount']:
            for i in  result.get('result')['tracks']:
                s1='%s'%(i['name'])
                s2='%s'%i['mp3Url']
                webcode=urllib.urlopen(s2).code
                #print webcode
                if webcode==404:
                    print '没有这首歌曲，妈蛋！！！'
                else:
                    muname = s1 + '.mp3'
                    finename = os.path.join(dir,muname)
                    urllib.urlretrieve(s2, finename)
                    print s1+u'下载完成'
                    num+=1
                    time.sleep(2)
    except TypeError:
        print '获取音乐失败没有这个数据'

def down(url):
    resp=urllib.urlopen(url).read()
#  print resp
    try:
        buf=StringIO(resp)
        f=gzip.GzipFile(fileobj=buf)
        data=f.read()
    except:
        data=resp
    result=json.loads(data)
    result_data=result.get('songs')
    try:
        music_name= result_data[0]['name'] #歌曲名称
        music_data=result_data[0]['mp3Url'] #MP3 文件下载地址
        print music_name
        print music_data
        dir = r'd:\music'
        webcode=urllib.urlopen(music_data).code
        if webcode==404:
            print '没有这首歌曲，妈蛋！！！'
        else:
            muname = music_name + '.mp3'
            finename = os.path.join(dir,muname)
            urllib.urlretrieve(music_data, finename)
            print music_name+u'下载完成'
    except IndexError:
        print '获取音乐失败没有这个数据'
if __name__ =='__main__':
    optMan()
    #songList('http://music.163.com/#/m/song?id=36924229&userid=61466625')
    #listUrl('http://music.163.com/#/m/playlist?id=62679396&userid=61466625')
    #songList('http://music.163.com/api/playlist/detail?id=62679396&updateTime=-1')
#muUrl('http://music.163.com/#/m/song?id=95991&userid=61466625')

