#!/usr/bin/env python
#-*- coding: utf-8 -*-
#__author__ = 'L34Rn'

from paramiko  import SSHClient
from paramiko  import AutoAddPolicy
from Queue     import Queue
from threading import Thread
from getopt    import getopt
from sys       import argv
from os        import _exit
from socket    import setdefaulttimeout
from os        import path
from time      import time
from time      import strftime


class send_exec(Thread):
    def __init__(self,q,type,cmd):
        Thread.__init__(self)
        self.q=q
        self.type=type
        self.cmd=cmd

    def run(self):
        global Results
        global view
        global l
        global i
        while 1:
            i+=1
            print '[+] [%s] [Running] [%s/%s] [%s%%]'%(strftime('%X'),str(i),str(l),str((i*100)/l))
            if self.q.empty()==True:
                break
            config=self.q.get()
            if self.get_config(config)=='Error':
                res='[%s]   [Error]\n'%strftime('%X')
                Results.append(res)
                if view==1:
                    print res
                continue
            else:
                host,port,username,password=self.get_config(config,self.type)
                result=self.ssh_exec(host,port,username,password)
                res='[%s]   [%s]\n%s\n'%(strftime('%X'),host,result)
                Results.append(res)
                if view==1:
                    print res

    def ssh_exec(self,host,port,username,password):
        try:
            ssh=SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(host,port,username, password)
            stdin, stdout, stderr = ssh.exec_command(self.cmd)
            result=stdout.readlines()
            ssh.close()
#           print '\n[+] [%s] [Runing] %s'%(strftime('%X'),result)
            return result
        except Exception,e:
            return e

    def get_config(self,config,type=0):
        # [email]root@127.0.0.1[/email][:22@password]
        try:
            if type==0:
                global PASSWORD
                temp=config.strip().split("@")
                if len(temp)>1:
                    username=temp[0]
                    if len(temp[1].split(':'))>1:
                        host=temp[1].split(':')[0]
                        port=int(temp[1].split(':')[1])
                    else:
                        host=temp[1]
                        port=22
                    return host,port,username,PASSWORD
                else:
                    return 'Error'
            elif type==1:
                temp=config.strip().split('@')
                if len(temp)>1:
                    username=temp[0]
                    if len(temp[1].split(':'))>1:
                        host=temp[1].split(':')[0]
                        port=int(temp[1].split(':')[1])
                    else:
                        host=temp[1]
                        port=22
                    if len(temp)>2:
                        password=temp[2]
                    else:
                        password=''
#                   print host,port,username,password
                    return host,port,username,password
                else:
                    return 'Error'
        except:
            return 'Error'

def usage():
    print '%-30s%s'%('[option]','[help]')
    print '%-30s%s'%('[======]','[====]')
    print '%-30s%s'%('[-h/--help]','[show this page and exit]')
    print '%-30s%s'%('[-l/--host-file]','[the host list file]')
    print '%-30s%s'%('[-p/--password]','[default password of ssh]')
    print '%-30s%s'%('[-e/--exec]','[the command to exec]')
    print '%-30s%s'%('[-t/--time-out]','[set default time-out]')
    print '%-30s%s'%('[-x/--threads]','[set threads number]')
    print '%-30s%s'%('[-o/--out-put]','[save result as a file]')
    print '%-30s%s'%('[-v/--view]','[show more details]')
    print '%-30s%s'%('[list format]','[[email]root@127.0.0.1[/email](:22@toor)]')

def main():
    if len(argv)< 3:
        usage()
        _exit(0)

    opts,args=getopt(
    argv[1:],
    'hl:p:e:t:x:o:v',
    [
    'help',
    'host-file=',
    'password=',
    'exec=',
    'time-out=',
    'threads=',
    'out-put=',
    'view'
    ])

    global PASSWORD
    global Results
    global view
    global l
    global i
    PASSWORD=''
    host_file=''
    cmd=''
    time_out=10
    x=1
    Results=[]
    threads=[]
    output_file=''
    type=1
    l=0
    i=0
    view=0

    for n,v in opts:
        if n in ('-h','--help'):
            usage()
            _exit(0)
        elif n in ('-l','--host-file'):
            host_file=v
        elif n in ('-p','--password'):
            PASSWORD=v
            type=0
        elif n in ('-e','--exec'):
            cmd=v
        elif n in ('-t','--time-out'):
            time_out=float(v)
        elif n in ('-x','--threads'):
            x=int(v)
        elif n in ('-o','--out-put'):
            output_file=v
        elif n in ('-v','--view'):
            view=1

    if host_file=='':
        print '[Error]  option -l/--host-file muset be required!'
        print '[Help]   use option -h/--help for more infomation!'
        _exit(0)

    if cmd=='':
        print '[Error]  option -e/--exec muset be required!'
        print '[Help]   use option -h/--help for more infomation!'
        _exit(0)

    print '[+] [%s] [Start]'% strftime('%X')

    setdefaulttimeout(time_out)

    print '[+] [%s] [Work] Set Defaulttimeout Ok!'%strftime('%X')

    q=Queue(maxsize=0)

    f=open(host_file,'r')
    lines=f.readlines()
    f.close()

    for line in lines:
        if line.strip()!='':
            l+=1
            q.put(line.strip())

    print '[+] [%s] [Work] Finished Queue Put!'%strftime('%X')

    for num in xrange(x):
        t=send_exec(q,type,cmd)
        threads.append(t)

    for th in threads:
        th.start()

    print '[+] [%s] [Work] All Threads Start Ok!'%strftime('%X')

    for th in threads:
        th.join()

    print '[+] [%s] [Work] All Done!'%strftime('%X')

    if output_file!='':
        if path.exists(output_file):
            output_dict_temp=output_file.split('.')[0:-1]
            output_dict_head=''
            for temp in output_dict_temp[0:-1]:
                output_dict_head+=temp+'.'
            output_dict_head+=output_dict_temp[-1]
            output_dict_end=output_file.split('.')[-1]
            output_file=output_dict_head+'_'+str(int(time()))+'.'+output_dict_end
        f=open(output_file,'a')
        for res in Results:
#           print res
            f.write(str(res)+'\n')
        f.close()
        print '[+] [%s] [Work] Result Save as %s'%(strftime('%X'),output_file)

    print '[+] [%s] [ShutDwon]'%strftime('%X')

if __name__ == '__main__':
    try:
        main()
    except Exception,e:
        print '[+] [%s] [Error] %s'%(strftime('%X'),str(e))
        print '[+] [%s] For more infotion use option -h/--help'%strftime('%X')