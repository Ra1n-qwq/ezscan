import os
import sys
import time
from .UseGetSubdomain import GetDomain
from .UsePortScan import PortScan
from .UseCheckURL import CheckURL
from .UseWebAnaylzer import Anaylzer

class Subdomain:
    def __init__(self):
        self.subdomain_file = 'F:/software/phpstudy2018/PHPTutorial/WWW/homework/scan/Output/subdomain.txt'

    def url_subdomain(self, url):
        Getdomain = GetDomain()
        Getdomain.url_Getdomain(url)

    def file_subdomain(self, targets_filename):
        Getdomain = GetDomain()
        Getdomain.file_Getdomain(targets_filename)

class Checkurl:
    def url_Check(self):  # 当两个模块一起使用的时候可以
        Checkurl = CheckURL()
        Checkurl.url_start()



class Portscan:
    def __init__(self):
        pass



    def syn_scan(self, hosts,start_port,end_port):
        starttime = time.time()
        syn_scan = PortScan()
        syn_scan.syn_scan(hosts,start_port,end_port)
        endtime = time.time()
        print('[TIME]The program is running time: %.2fs' % (endtime - starttime))


class Webanaylzer:
    def one_analyzer(self, target_url):
        w = Anaylzer()
        w.one_module_start(target_url)

    def url_analyzer(self):
        w = Anaylzer()
        w.url_start()
    def file_analyzer(self, targets_file):
        w = Anaylzer()
        w.file_start(targets_file)

