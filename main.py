import nmap
from getmac import get_mac_address
class Network(object):
    def __init__(self,ip=''):
        ip=input("please enter ip address:")
        self.ip=ip

    def get_mac_address(self,IP=''):
        mac = get_mac_address(IP)


    def networkScanner(self):
        if len(self.ip)==0:
            network='192.168.1.1/24'
        else:
            network=self.ip+'/24'
        print('Scanning please wait --->')
        nm=nmap.PortScanner()
        nm.scan(hosts=network,arguments='-sn')
        hosts_list=[(x,nm[x]['status']['state'])for x in nm.all_hosts()]
        for host,status in hosts_list:
            mac = self.__Get_Mac(IP=host)
            print("Host\t{}\tMAC:{}".format(host,mac))

if __name__== "__main__":
    D = Network()
    D.networkScanner()

