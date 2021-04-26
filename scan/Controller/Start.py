import os
import time
from .Controller import Subdomain, Checkurl, Portscan, Webanaylzer


class IGScan:
    def __init__(self, url, targets_file, hosts, port, module):
        self.url = url
        self.port = port
        self.targets_file = targets_file
        self.hosts = hosts
        self.module = module
        self.Subdomain = Subdomain()
        self.Checkurl = Checkurl()
        self.PortScan = Portscan()
        self.Webanaylzer = Webanaylzer()

    def Start(self):
        url = self.url
        targets_file = self.targets_file
        hosts = self.hosts
        start_port = int(self.port[0])
        end_port = int(self.port[1])
        module = self.module
        Subdomain = self.Subdomain
        Checkurl = self.Checkurl
        Portscan = self.PortScan
        Webanaylzer = self.Webanaylzer
        if not os.path.exists('Output/'):
            os.mkdir('Output/')
        if module != '' and module != None:
            module = module.split(',')
            if url != '' and url != None:
                all_module = ['subdomain', 'checkurl', 'webanalyzer']
                inse_module = list(set(all_module).intersection(set(module)))  # 交集
                dif_module = list(set(all_module).difference(set(module)))  # 并集
                # print(module)
                if len(dif_module) == 0:   #调用模块x1
                    starttime = time.time()
                    Subdomain.url_subdomain(url)
                    Checkurl.url_Check()
                    Webanaylzer.url_analyzer()
                    endtime = time.time()
                    print('[SUCC] All target links have been collected!')
                    print('[TIME] The program is running time: %.2fs' % (endtime - starttime))

                if len(dif_module) == 1:
                    if module[0] == 'subdomain':  #调用模块x2
                        starttime = time.time()
                        Subdomain.url_subdomain(url)
                        Checkurl.url_Check()
                        endtime = time.time()
                        print('[SUCC] All target links have been collected!')
                        print('[TIME] The program is running time: %.2fs' % (endtime - starttime))
                    if module[0] == 'webanalyzer':
                        starttime = time.time()
                        Subdomain.url_subdomain(url)
                        Checkurl.url_Check()
                        endtime = time.time()
                        print('[SUCC] All target links have been collected!')
                        print('[TIME] The program is running time: %.2fs' % (endtime - starttime))

                if len(inse_module) == 1:  #调用模块x3
                    if module[0] == 'subdomain':
                        starttime = time.time()
                        Subdomain.url_subdomain(url)
                        endtime = time.time()
                        print('[SUCC] All target links have been collected!')
                        print('[TIME] The program is running time: %.2fs' % (endtime - starttime))
                    elif module[0] == 'checkurl':
                        starttime = time.time()
                        Checkurl.url_Check()
                        endtime = time.time()
                        print('[SUCC] All target links have been collected!')
                        print('[TIME] The program is running time: %.2fs' % (endtime - starttime))
                    elif module[0] == 'webanalyzer':
                        starttime = time.time()
                        Webanaylzer.one_analyzer(url)
                        endtime = time.time()
                        print('[SUCC] All target links have been collected!')
                        print('[TIME] The program is running time: %.2fs' % (endtime - starttime))
        if hosts != '' and hosts != None:
            Portscan = Portscan
            Portscan.syn_scan(hosts,start_port,end_port)
