#!/usr/bin/env python
#-*- coding: utf-8 -*-
#__author__ = 'Ario'

import urllib2
import socket


def assign(service, arg):
    if service == "path":
        return True, arg

def audit(arg,file):
    url = arg
    path_list=read_dict(file)
    # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
    # socket.socket = socks.socksocket
    for path in path_list:
        request = urllib2.Request(url+path)
        request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
        try:
            response = urllib2.urlopen(request,timeout=10)
            code=response.getcode()
            if code==200:
                print(url+path)
        except urllib2.URLError,e:
            print e
        except socket.timeout,e:
            print type(e)

def audit_with_http_proxy(arg,file):
    url = arg
    path_list=read_dict(file)
    proxy_addr='218.64.255.253:3128'
    proxy_handler = urllib2.ProxyHandler({'http':proxy_addr})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    for path in path_list:
        request = urllib2.Request(url+path)
        request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
        try:
            f = urllib2.urlopen(request,timeout=10)
            if f:
                print(url+path)
        except urllib2.URLError,e:
            print "."
        except socket.timeout,e:
            print type(e)

def read_dict(file):
    lines=[]
    with open(file, 'r') as f:
        for line in f:
            lines.append(line)
    return lines

if __name__ == '__main__':
    audit(assign('path', 'http://localhost')[1],'asp.txt')
    # audit_with_http_proxy(assign('path', 'http://localhost')[1],'asp.txt')