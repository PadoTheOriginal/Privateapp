import socket
from os import popen
from re import search


class SearchServer:
    socket.setdefaulttimeout(0.1)
    # ""
    @staticmethod
    def connect(str hostname, int port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((hostname, port))
        
        if res == 0:
            sock.settimeout(None)
            return sock 

        else: return False




    def look_for_server(self, int port, recent_servers=[]):
        ips = []
        ips += recent_servers

        for device in popen('arp -a'):
            ip = search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', device)
            if ip:
                ip_found = ip.group(0)
                ips.append(ip_found)

        for ip in ips:
            res = self.connect(ip, port)
            if res: return res, ip

        return 1, 1


# ""
if __name__ == "__main__":
    ipFound = SearchServer().look_for_server(3737)
    if ipFound != 1: 
        print("Device found at : ", ipFound)
