#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @author   xds
# @date     2016-1-28
# @note     url管理器

import random

class UrlManager(object):
    def __init__(self, num):
        start = 1000 * num
        end = start + 999
        b_list = range(start, end)
        self.new_urls = random.sample(b_list, 999)
        self.old_urls = []

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.append(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.append(new_url)
        return new_url
