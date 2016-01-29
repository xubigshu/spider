#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @author   xds
# @date     2016-1-28
# @note     保存解析的结果,将解析结果保存到mysql

import MySQLdb

class HtmlOutputer(object):
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host='localhost',user='root',passwd='juchongai',port=3306, charset="utf8")
            self.cur = self.conn.cursor()
            
            # self.cur.execute('create database if not exists xiami')
            self.conn.select_db('xiami')
            # self.cur.execute('create table songinfo(id varchar(8), name varchar(128), lyric text, album varchar(128), singer varchar(128), tag varchar(128))')
             
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])


    def persist_data(self, id,name, lyric, album, singer, tag):
        try:
            # print "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
            # print type(name)
            # print name
            # print type(('\n').join(lyric))
            # print ('\n').join(lyric)
            # print "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
            #主键id是自增的，插入时用空字符串代替
            print name
            print lyric
            print album
            print singer
            print tag
            tag = ('-').join(tag)
            if len(tag) == 0:
                tag = ""
            sql = 'insert into songinfo(id, name, lyric, album, singer, tag) values("' + str(id) +'","' + name +  '","' + ('\n').join(lyric) + '","' + album + '","' + singer + '","' + tag + '")'

            print "wwwwwwwwwwwwwwwwwww"
            print sql
            print type(sql)

            sql = sql.encode('utf8')

            

            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print e

    def db_commit_close(self):
        try:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except Exception as e:
            pass