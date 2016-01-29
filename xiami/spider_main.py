#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @author   xds
# @date     2016-1-28
# @note     程序入口

import threading
import thread
import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):
    def __init__(self, num):
        self.urls = url_manager.UrlManager(num)
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 0
        while self.urls.has_new_url():
            try:

                tmp = self.urls.get_new_url()
                new_url = root_url +  str( tmp )
                
                print "**********************"
                print("url: %s" %(new_url))
                code, html_doc = self.downloader.download(new_url)
                if code != 1:
                    continue


                #必须先更新parser中的soup
                self.parser.update_soup(html_doc)
                    
                #获取歌名
                name = self.parser.get_song_name()


                #获取歌词
                lyric = self.parser.get_song_lyric()

                #获取专辑和演唱者
                album, singer = self.parser.get_song_album_singer()
                
                #获取所属标签
                tag_list = self.parser.get_song_tag()
                

                #将爬去的数据存储起来
                print "将爬去的数据存储起来"
                self.outputer.persist_data(tmp, name, lyric, album, singer, tag_list)

                #成功抓取了1000个以后，结束程序
                count = count + 1
                if count == 1000:
                    break
            except:
                print('craw failed')



        #将数据commit，同时关闭数据库连接
        self.outputer.db_commit_close()

def main():
    root_url = "http://www.xiami.com/song/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

def run(i):
    root_url = "http://www.xiami.com/song/"
    obj_spider = SpiderMain(i)
    obj_spider.craw(root_url)

if __name__ == '__main__':
    # main()

    all_thread = []
    for i in range(0, 10):
        t = threading.Thread(target=run, args=(i,))
        all_thread.append(t)
        t.start()

    for t in all_thread:
        t.join()
