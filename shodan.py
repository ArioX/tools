#!/usr/bin/python
# Exploit toolkit using shodan module for search exploit & host lookup
# Code : by jimmyromanticdevil
#
# Download :
#   Before you run this code you must install shodan lib.
#   $ wget [url]http://pypi.python.org/packages/source/s/shodan/shodan-0.4.tar.gz[/url]
#   $ tar xvf shodan-0.2.tar.gz
#   $ cd shodan-0.2/
#   $ sudo python setup.py install
# Api key request:
#   See in here : [url]http://www.shodanhq.com/api_doc[/url]
# Rules of shodan :
#    1. Don't make more than 1 query per second.
#    2. Be respectful when using the API, I don't have a lot of resources to work with.
#    So users might want to get their own key (have to register on shodan's website).
#    Plus all the requests go through shodan servers which might make it pretty slow if many people are using the service. 
#  
# Special thanks :
#          thanks person :5ynl0rd,kiddies aka peneter,ne0 d4rk fl00der,oghie,parc0mx,me0nkz,suryal0e,zee_eichel
#                         mirwan aka cassaprogy,shadow_maker,suddent_death,aip,r3d3,dawflin,n1nj4,hakz,
#                         leXel,s3my0n,MaXe,Andre Corleone ,Shamus,and all my friend .
#          thanks communty : Tecon-crew<[url]http://tecon-crew.org[/url]>
#                            Void-labs <[url]http://void-labs.org[/url]>
#                            Makassar ethical hacker<[url]http://makassarhacker.com/>[/url]
#                            Intern0t <[url]http://forum.intern0t.net/>[/url]
#                            Deadc0de <[url]http://forum.deadc0de.or.id/>[/url]
#-----------------------------------------------
import shodan,sys,time,base64,os
from time import sleep
from shodan import WebAPI
 
__author__='amltbXlyb21hbnRpY2Rldmls'
__email__ ='PHJvbWFudGljZGV2aWwuamltbXlAZ21haWwuY29tPg=='
__api__   ='Z4xjUqqsaQbFgYrnn3EBuoJsSC0VZTyI'#request youre api key  and paste in here 
_lolz_    = WebAPI(__api__)
 
 
 
def tayping(title):
    try:
       for i in title:
          print "\b%s"%i,
          sys.stdout.flush()
          time.sleep(0.005) 
    except ImportError:
       print "Some Error",
 
def check():
     try:
        checking = "[C]Checking module..."
        tayping(checking)
        sleep(2)
        import shodan
     except ImportError:
        error ="\n[!]You must install Shodan Module in here :\n[url]http://pypi.python.org/packages/source/s/shodan/...[/url]"
        tayping(error_module)
     except KeyboardInterrupt:
    print "\n[*]Exiting program...\n"
    sys.exit(1)
     else :
        succes="\n[*]Shodan module is available..."
        tayping(succes)
        sleep(2)
     try:
        api_check="\n[C]Checking Api key.."
        tayping(api_check)
        sleep(2)
        check_Api = len(__api__)
        if check_Api==0:
           error_api=  "\n[!] Api key is not available\n[!]You must request Api key in here :[url]http://www.shodanhq.com/api_doc[/url]\n\n\n\n"
           tayping(error_api)
           sleep(2)
        elif check_Api != 0:
           succces = "\n[*]Api key is available\n\n\n\n"
           tayping(succces)
           sleep(3)
     except KeyboardInterrupt:
    print "\n[*] Exiting program...\n"
    sys.exit(0)
    
            
          
 
def clear():
    if sys.platform in ('linux-i386', 'linux2', 'darwin'):
        SysCls = 'clear'
    elif sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
        SysCls = 'cls'
    else:
        SysCls = 'unknown'
 
    return SysCls
 
def title():
         __Auth__= base64.b64decode(__author__)
         __Eml__ = base64.b64decode(__email__)
         title='''
//////////////////////////////////////////////////////
___________                .__           .__   __
\_   _____/___  _________  |  |    ____  |__|_/  |_
 |    __)_ \  \/  /\____ \ |  |   /  _ \ |  |\   __\\
 |        \ >    < |  |_> >|  |__(  <_> )|  | |  |
/_______  //__/\_ \|   __/ |____/ \____/ |__| |__|
        \/       \/|__|/
                                   Toolkit
 
Coder by : %s
Contach  : %s
//////////////////////////////////////////////////////
'''%(__Auth__,__Eml__)
         tayping(title)
 
 
def expoitdb():
        try:
           searching_Exploit= raw_input('[+]Search a exploit :')
           print '[!]You search [%s] Exploit'% searching_Exploit
           wtf     = _lolz_.exploitdb.search(searching_Exploit)
           more    = wtf['total']
           print '[!]Found [%s] exploit with result [%s]'%(more,searching_Exploit)
           try:
              display =raw_input('[!]See all list exploit found?(y/n)')
              if display =='y':
                    ds = wtf['matches']
                    for i in ds :
                        print'%s: %s' % (i['id'],i['description'])
           except Exception,err:
                  print'[%s]'%err
 
           try:
              display_exploit=raw_input('[+]Select type exploit?(y/n)')
              if display_exploit =='y':
                 print'choois types : remote, webapps, dos, local, shellcode ?'
                 rock =raw_input('')
                 print 'youre chooise [%s] exploits'%rock
                 r = wtf['matches']
                 for i in r:
                     if rock ==i['type']:
                           print'%s: %s' % (i['id'],i['description'])
           except Exception,err:
                   print'[%s]'%err
           try:
              view_exploit=raw_input('[+]Select exploit to view ?(y/n)')
              if view_exploit =='y':
                 print'[+]Enter exploit id to view :'
                 v = raw_input('')
                 lols=wtf['matches']
                 for i in lols:
                     if v == str(i['id']):
                        File_exploit = _lolz_.exploitdb.download(i['id'])
                        print 'Filename: %s'% File_exploit['filename']
                        print 'Content-type: %s' % File_exploit['content-type']
                        print File_exploit['data']
                        download_exploit= raw_input('[+]download the exploit ?(y/n)')
                        if download_exploit=='y':
                           dwnload = open(File_exploit['filename'], 'w')
                           dwnload.write(File_exploit['data'])
                           dwnload.close()
                           print'%s successfully download' % File_exploit['filename']
           except Exception,err:
                   print'[%s]'%err
           try_again=raw_input('[+]Do you want to try again ?(y/n):')
           while try_again=='y':
              os.system(clear())
              title()
              expoitdb()
              try_again=raw_input('[+]Do you want to try again ?(y/n):')
           main()
        except KeyboardInterrupt, IOError:
                 print '\nYou pressed Ctrl+C or exited...'
                 main()
             sys.exit(1)
 
def metasploit():
        try:
           module_search=raw_input('[!]Search module metasploit :')
           print'[!]We will search metasploit module'
           m_m     = _lolz_.msf.search(module_search)
           result  = m_m['total']
           print 'Modules found: %s'%result
           result2 = m_m['matches']
           for i in result2:
              print '%s: %s' % (i['type'], i['name'])
              download =raw_input('[+]Download module : (y/n)')
              if download =='y':
                 file = _lolz_.msf.download(i['fullname'])
                 print 'Filename: %s' % file['filename']
                 print 'Content-type: %s' % file['content-type']
                 print file['data']
           try_again = raw_input('[+]Do you want to try again ?(y/n)')
           while try_again =='y':
                 os.system(clear())
                 title()
                 metasploit()
                 try_again = raw_input('[+]Do you want to try again ?(y/n)')
           main()
        except Exception,err:
           print'[%s]'%err
 
def host():
        try:
          input_host  = raw_input('[+]Input host :')
          host_result = _lolz_.host(input_host)
          ip     =host_result['ip']
          country=host_result.get('country', None)
          city   =host_result.get('city', None)
          host_name =host_result['hostnames']
          data   =host_result['data']
          resulting ="""
                Ip addres = %s
                Country   = %s
                City      = %s
                """%(ip,country,city,)
          tayping(resulting)
          for i in data :
              print """
                 Port     = %s
                 Banner   = %s"""%(i['port'],i['banner'])
          try_again = raw_input('[!]try again ?(y/n)')
          while try_again =='y':
                host()
                try_again = raw_input('[!]try again ?(y/n)')
        except Exception,err:
              print'[%s]'%err
              main()
 
def exit():
      teks_exit='\nExiting..\nThanks for use this tools'
      tayping(teks_exit)
      sleep(2)
      sys.exit()
 
def main():
        try:
           os.system(clear())
           title()
           menu = {'1':expoitdb, '2':metasploit, '3':host, '4':exit,}
           while True:
               print """
Input your chooise:
1) Search exploit
2) Search Metasploit Modules
3) Host lookup
4) Exit
"""
               try:
                  chooise = raw_input('Select you chooise: ')
               except KeyboardInterrupt, IOError:
                 print '\nYou pressed Ctrl+C or exited...'
             sys.exit(1)
               else:
                  if chooise in menu.keys():
                 menu[chooise]()
                     os.system(clear())
                     title()
              else:
                 print '\nInvalid selection'
 
        except Exception,err:
              print'[%s]'%err
 
if __name__=='__main__':
     check()
     main()