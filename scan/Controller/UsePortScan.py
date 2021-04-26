from Core.PortScan import Synscan


class PortScan:

    def __init__(self):
        pass

    def syn_scan(self, hosts,start_port,end_port):
        syn_scan = Synscan(hosts,start_port,end_port)
        syn_scan.syn_scan()