from Utils.Webanaylzer import Webanalyzer
import queue
import threading
import time
q = queue.Queue()
class Anaylzer:
    def __init__(self):
        self.webanalyzer = Webanalyzer()
        self.link_file = "./Output/link.txt"

    def anaylzer(self, total_num):
        starttime = time.time()
        while not q.empty():
            get_url = q.get()
            endtime = time.time()
            program_time = (endtime-starttime)
            w = self.webanalyzer
            w.arr_res(target_url=get_url)


    def one_module_start(self, target_url):
        print('[INFO] Webanaylzer Module Running!')
        w = self.webanalyzer
        w.one_arr_res(target_url)

    def url_start(self):
        thread_list = []
        print('[INFO] Webanaylzer Module Running!')
        with open("./Output/fingerprint.txt","w") as f1:
            f1.close()
        with open(self.link_file, 'r',encoding='utf-8') as f:
            for i in f.readlines():
                q.put(i.strip('\n'))
        total_num = q.qsize()  # 获取所有链接数目 http/https
        print('[INFO] The total number of targets to be detected is: %d' % total_num)  # 要获取的链接总数为
        for i in range(15):
            t = threading.Thread(target=self.anaylzer, args=(total_num, ))
            thread_list.append(t)
        for t in thread_list:
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        print('[SUCC] Webanaylzer Module Has Finished Running!')

    def file_start(self, targets_file):
        thread_list = []
        print('[INFO] Webanaylzer Module Running!')
        with open("./Output/fingerprint.txt","w") as f1:
            f1.close()
        with open(targets_file, 'r',encoding='utf-8') as f:
            for i in f.readlines():
                q.put(i.strip('\n'))
        total_num = q.qsize()  # 获取所有链接数目 http/https
        print('[INFO] The total number of targets to be detected is: %d' % total_num)  # 要获取的链接总数为
        for i in range(15):
            t = threading.Thread(target=self.anaylzer, args=(total_num,))
            thread_list.append(t)
        for t in thread_list:
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        print('[SUCC] Webanaylzer Module Has Finished Running!')