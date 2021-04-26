# -*- coding:utf-8 -*-
import sys
import threading
import random
from queue import Queue
from optparse import OptionParser
import requests


class WebDirScan:
  """
  Web目录扫描器
  """

  def __init__(self, options):
    self.url = options.url
    # self.file_name = options.file_name
    self.count = options.count

  class DirScan(threading.Thread):
    """
    多线程
    """

    def __init__(self, queue, total):
      threading.Thread.__init__(self)
      self._queue = queue
      self._total = total

    def run(self):
      while not self._queue.empty():
        url = self._queue.get()
        try:
          r = requests.get(url=url, headers=get_user_agent(), timeout=5)#模拟用户发送request请求
          if r.status_code == 200:
            # print( '[+]%s' % url)
            print( '[+]%s' % url)#输出爆破出的网站目录
            # 保存到本地文件，以HTML的格式
            result = open('./Output/result.html', 'a+')
            dirlist.append(url)
            result.write('<a href="' + url + '" rel="external nofollow" target="_blank">' + url + '</a>')
            result.write('\r\n</br>')
            result.close()
        except Exception:
          pass


  def start(self):
    result = open('./Output/result.html', 'w')
    
    result.close()
    queue = Queue()
    f = open('./Core/dic.txt', 'r',encoding='utf-8')#根据预先设置的字典进行爆破
    for i in f.readlines():
      queue.put(self.url  + i.rstrip('\n'))
    total = queue.qsize()
    threads = []
    thread_count = int(self.count)
    for i in range(thread_count):
      threads.append(self.DirScan(queue, total))
    for thread in threads:
      thread.start()
    for thread in threads:
      thread.join()


def get_user_agent():
  """
  User Agent的细节处理
  :return:
  """
  user_agent_list = [
    {'User-Agent': 'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; en) Opera 11.00'},
    {
      'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.0.2'},
    {
      'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.1.15) Gecko/20101027 Fedora/3.5.15-1.fc12 Firefox/3.5.15'},
    {
      'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.551.0 Safari/534.10'},
    {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008092809 Gentoo Firefox/3.0.2'},
    {
      'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.544.0'},
    {'User-Agent': 'Opera/9.10 (Windows NT 5.2; U; en)'},
    {
      'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko)'},
    {'User-Agent': 'Opera/9.80 (X11; U; Linux i686; en-US; rv:1.9.2.3) Presto/2.2.15 Version/10.10'},
    {
      'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9b3) Gecko/2008020514 Firefox/3.0b3'},
    {
      'User-Agent': 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; fr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'},
    {
      'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'},
    {
      'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.60'},
    {
      'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51'}
  ]

  return random.choice(user_agent_list)


def main():
  parser = OptionParser('Please input  URL Correct!')
  parser.add_option('-u', '--url', dest='url', type='string')
  # parser.add_option('-f', '--file', dest='file_name', type='string', help='dictionary filename')
  parser.add_option('-t', '--thread', dest='count', type='int', default=20)
  (options, args) = parser.parse_args()
  if options.url :
    if "http://" in options.url or "https://" in options.url:
      dirscan = WebDirScan(options)
      dirscan.start()
      if not dirlist:
        print("[+]    无")
    else:
      print("URL ERROR")
      sys.exit(1)
  else:
    print("Please input  URL Correct!")
    sys.exit(1)


if __name__ == '__main__':
  dirlist=[]
  main()
