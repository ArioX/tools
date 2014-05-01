#!/usr/bin/env python
#-*- coding: utf-8 -*-
#__author__ = 'Ario'

import urllib2
import socket
import socks


def set_socks5_proxy():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket


def set_http_proxy():
    proxy_addr='218.64.255.253:3128'
    proxy_handler = urllib2.ProxyHandler({'http':proxy_addr})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)

def audit(host,file,proxy):
    if proxy=='socks5':
        set_socks5_proxy()
    elif proxy=='http':
        set_http_proxy()
    path_list=read_dict(file)
    for path in path_list:
        request = urllib2.Request(host+path)
        request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
        try:
            response = urllib2.urlopen(request,timeout=10)
            code=response.getcode()
            if code==200:
                print(host+path)
        except urllib2.URLError,e:
            # print '.'
            pass
        except socket.timeout,e:
            print type(e)

def read_dict(file):
    lines=[]
    with open(file, 'r') as f:
        for line in f:
            lines.append(line)
    return lines

if __name__ == '__main__':
    host="http://localhost/"
    dict="asp.txt"
    proxy='http'
    audit(host,dict,proxy)