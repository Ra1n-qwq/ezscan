# -*- encoding: utf-8 -*-
#coding=utf-8
import threading
from scapy.all import *
import time
lock = threading.Lock()

class Synscan:


    def __init__(self, hosts,start_port,end_port):
        self.hosts = hosts
        self.start_port=start_port
        self.end_port=end_port
    def syn_scan(self):
        self.alive_port=[]
        thread_list2=[]
        for port in range(self.start_port,self.end_port+1):   #调用多线程进行syn端口探测
            t2=threading.Thread(target=self.syn_scan_start,args=(self.hosts,port))
            thread_list2.append(t2)
        for t in thread_list2:
            t.setDaemon(True)
            t.start()
        for t in thread_list2:
            t.join()
        if self.alive_port:
            print('[****]IP：%s   开放端口：%s'%(self.hosts,",".join(self.alive_port)))
        else:
            print('[****]IP：%s   开放端口：无'%(self.hosts))
    def syn_scan_start(self,target_ip,port):#利用scapy构造数据包
        a = sr1(IP(dst=target_ip) / TCP(dport=port), timeout=1, verbose=0)
        if a == None:
            pass
        else:
            try:
                if int(a[TCP].flags) == 18: #根据返回包长度判断是否存活
                    lock.acquire()
                    self.alive_port.append(str(port)) #线程锁防止端口错误
                    lock.release()
                else:
                    pass
            except IndexError:
                pass
