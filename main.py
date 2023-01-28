import socket
import nmap
from getmac import get_mac_address


class Network(object):
    def init(self, ip=''):
        ip = input("please enter ip address (or press enter for default) : ")
        self.ip = ip

    def get_mac(self, IP=''):
        mac = get_mac_address(IP)

    def networkScanner(self):
        if len(self.ip) == 0:
            network = '192.168.1.1/24'
        else:
            network = self.ip + '/24'
        print('Scanning please wait --->')

        # here you need to set the nnmap_path correctly !
        nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe", ]

        nm = nmap.PortScanner(nmap_search_path=nmap_path)
        nm.scan(hosts=network, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            mac = self.get_mac(IP=host)
            print("Host\t{}\tMAC:{}".format(host, mac))


if __name__ == "main":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    D = Network()
    D.networkScanner()