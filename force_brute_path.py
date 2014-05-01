#!/usr/bin/env python
#-*- coding: utf-8 -*-
#__author__ = 'Ario'

from optparse import OptionParser
import urllib2
import socket
import socks

def set_socks5_proxy():
    '''
    set the socks5 proxy
    '''
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080) #todo: read from a proxy list file
    socket.socket = socks.socksocket


def set_http_proxy():
    '''
    set the http proxy
    '''
    proxy_addr='218.64.255.253:3128' #todo:read from a proxy list file
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
                print(host+path) #todo:write log,save the successful results
        except urllib2.URLError,e:
            # print '.'
            pass
        except socket.timeout,e:
            print type(e)  #todo:try another proxy if the current proxy tunnel is timeout

def read_dict(file):
    lines=[]
    with open(file, 'r') as f:
        for line in f:
            lines.append(line)
    return lines

def main():
    options = OptionParser(usage='%prog url [options]', description='Test for path brute force attack')
    options.add_option('-d', '--dict', type='string', default='php.txt', help='dictionary of path for using')
    options.add_option('-p', '--proxy', type='string', default='http', help='proxy type:http,socks5')
    opts, args = options.parse_args()
    if len(args) < 1:
        options.print_help()
        return
    audit(args[0],opts.dict,opts.proxy)


if __name__ == '__main__':
    main()