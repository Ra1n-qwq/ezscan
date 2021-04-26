# -*- encoding: utf-8 -*-
import argparse
import re
from Controller.Start import IGScan

parser = argparse.ArgumentParser(description="IGScan (Information Gathering Scan)")
parser.add_argument('-u', '--url', help='Taget URL')
parser.add_argument('-f', '--file', help='Place files for all domain names')
parser.add_argument('-i', '--ip', help='192.168.2.1 or 192.168.2.1-192.168.2.10')
parser.add_argument('-p', '--port', help='1-65535',default='1-1000')
parser.add_argument('-m', '--module', help='Select the module to detect the target', default='subdomain,checkurl,webanalyzer')  # 选择模块对目标进行探测

args = parser.parse_args()  # 实例化
targets_file = args.file
hosts = args.ip
port = args.port.rsplit('-',1)
url = args.url
module = args.module
#print(11)


if module=="webanalyzer":
    if re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[.+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',url):
        IGScan = IGScan(url, targets_file, hosts, port, module)
        IGScan.Start()
    else:
        print("请检查输入的url")
else:
    IGScan = IGScan(url, targets_file, hosts, port, module)
    IGScan.Start()
# #测试
# #IGScan = IGScan(url, targets_file, "192.168.43.1", port, module)
# #IGScan=IGScan("bilibili.com",targets_file,hosts,port,"subdomain,checkurl,webanalyzer")


