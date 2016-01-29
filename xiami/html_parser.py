#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @author   xds
# @date     2016-1-28
# @note     解析所要的结果

from bs4 import BeautifulSoup
import re
import sys


class HtmlParser(object):
    def __init__(self):
        pass

    def update_soup(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

    def get_song_name(self):
        '''获取歌名'''
        links = self.soup.find_all('h1')
        # for link in links:
        #     print link.encode('utf8')
        # return links[0].get_text().encode('utf8')
        return links[0].get_text()

    def get_song_lyric(self):
        '''获取歌词'''
        lrc_list = []
        links = self.soup.find_all("div", {"class":"lrc_main"})
        for link in links:
            # lrc = link.get_text().encode('utf8').strip()
            lrc = link.get_text().strip()
            if lrc.startswith("startswith"):
                continue
            elif len(lrc) == 0:
                continue
            elif lrc.startswith("<br"):
                continue
            else:
                lrc_list.append(lrc)
        return lrc_list

    def get_song_album_singer(self):
        '''获取专辑和演唱者'''
        links = self.soup.find_all("div", attrs={"style":"white-space:nowrap; width:140px; overflow:hidden; text-overflow:ellipsis;"})
        # album = links[0].get_text().encode('utf8').strip()
        # singer = links[1].get_text().encode('utf8').strip()
        album = links[0].get_text().strip()
        singer = links[1].get_text().strip()
        return album, singer

    def get_song_tag(self):
        '''所属标签'''
        tag_list = []
        links = self.soup.find_all("a", attrs={"class":re.compile(r"hot(\w+)")})
        for link in links:
            # tag_list.append( link.get_text().encode('utf8') ) 
            tag_list.append( link.get_text() ) 

        return tag_list
