import threading
import time
import requests
import requests.packages.urllib3
import queue
import random


class RequestsURL:

    def __init__(self):
        self.subdomain_filename = './Output/subdomain.txt'
        self.link_filename = './Output/link.txt'
        self.link_num = 0
        self.putsubdomain_queue = queue.Queue()  # 放置子域名的队列
        self.putsurvival_queue = queue.Queue()  # 放置存活域名的队列，用于写入result.txt

    def get_random_headers(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        return random.choice(user_agent_list)

    def getURL(self, total_num):
        starttime = time.time()
        putsubdomain_queue = self.putsubdomain_queue
        putsurvival_queue = self.putsurvival_queue
        headers = {"User-Agent": self.get_random_headers()} #构造header
        while not putsubdomain_queue.empty():
            get_url = putsubdomain_queue.get()
            try:
                http_url = "http://" + get_url
                requests.packages.urllib3.disable_warnings()  #
                http_res = requests.get(url=http_url, headers=headers, timeout=1, verify=False)
                if http_res.status_code == 200:#根据状态码判断是否存活
                    putsurvival_queue.put(http_url)
                    self.link_num += 1  # 计数有多少link
            except:
                pass
            try:
                https_url = "https://" + get_url
                requests.packages.urllib3.disable_warnings()  #
                https_res = requests.get(url=https_url, headers=headers, timeout=1, verify=False)
                if https_res.status_code == 200:
                    putsurvival_queue.put(https_url)
                    self.link_num += 1
            except:
                pass

    def url_start(self):
        print('[INFO] CheckDomain Module Running!')
        subdomain_filename = self.subdomain_filename
        link_filename = self.link_filename
        putsubdomain_queue = self.putsubdomain_queue
        putsurvival_queue = self.putsurvival_queue
        thread_list = []
        with open(subdomain_filename, 'r',encoding='utf-8') as f:
            for subdomain in f.readlines():
                putsubdomain_queue.put(subdomain.strip('\n'))
        total_num = putsubdomain_queue.qsize()  # 获取子域名的总数
        for i in range(50):
            t = threading.Thread(target=self.getURL, args=(total_num, ))
            thread_list.append(t)
        for t in thread_list:
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        f = open(link_filename, 'w',encoding='utf-8')
        while not putsurvival_queue.empty():
            put_url = putsurvival_queue.get()
            print(put_url)
            f.write(put_url+'\n')
        f.close()
        print('[SUCC] CheckDomain Module Has Finished Running!')
        print('[INFO] The number of links obtained is: %d' % self.link_num)
