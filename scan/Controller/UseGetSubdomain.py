import time
from Core.GetSubdomain import GetSubdomain
import queue
import threading


class GetDomain:

    def __init__(self):
        self.subdomain_num = 0
        self.targets_queue = queue.Queue()
        self.arr_subdomain = []  # 去重后的域名
        self.subdomain_filename = './Output/subdomain.txt'  # 子域名result
        self.GetSubdomain = GetSubdomain()

    # -u参数
    def url_Getdomain(self, url):
        print('[INFO] GetDomain Module Running!')
        open_subdomainfile = open(self.subdomain_filename, 'w',encoding='utf-8')
        arr_subdomain = self.arr_subdomain
        url = url.strip('\n')
        GetSubdomain = self.GetSubdomain
        for i in GetSubdomain.all2one(url):
            arr_subdomain.append(i)
        arr_subdomain = list(set(arr_subdomain))
        self.subdomain_num = len(arr_subdomain)
        for i in arr_subdomain:
            open_subdomainfile.write(i+'\n')
            # print(i)    #输出子域名
        open_subdomainfile.close()
        print('[INFO] Number of subdomains: %s' % (self.subdomain_num))
        print('[SUCC] GetDomain Module Has Finished Running!')

    # -f参数
    def file_Getdomain(self, targets_filename):
        # --定义header头
        starttime = time.time()
        targets_queue = self.targets_queue
        print('[INFO] GetDomain Module Running!')
        open_subdomainfile = open(self.subdomain_filename, 'w',encoding='utf-8')  # 写入subdomain.txt文件
        arr_subdomain = self.arr_subdomain
        with open(file=targets_filename, mode='r',encoding='utf-8') as domain:
            for url in domain.readlines():
                url = url.strip('\n')
                targets_queue.put(url)
        total_num = targets_queue.qsize()
        print('[INFO] The total number of targets to be detected is: %d' % total_num)
        GetSubdomain = self.GetSubdomain
        thread_list = []
        def thread_file_Getdomain():
            while not targets_queue.empty():
                get_url = targets_queue.get()
                endtime = time.time()
                program_time = (endtime - starttime)
                threading.Thread(target=self.file_Getdomain_progress, args=(total_num, program_time,)).start()
                for i in GetSubdomain.all2one(get_url):
                    arr_subdomain.append(i)
        for i in range(15):
            t = threading.Thread(target=thread_file_Getdomain)
            thread_list.append(t)
        for t in thread_list:
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        # --- 域名去重
        arr_subdomain = list(set(arr_subdomain))
        self.subdomain_num = len(arr_subdomain)
        for i in arr_subdomain:
            open_subdomainfile.write(i+'\n')
            print(i)   #输出子域名
        open_subdomainfile.close()
        print('\n[INFO] Number of subdomains: %s' % (self.subdomain_num))
        print('[SUCC] GetDomain Module Has Finished Running!')
