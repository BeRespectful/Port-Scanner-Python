import socket

def scanNetwork(ip,startPort,endPort):
    print("[*]Starting port scanning on host:",ip )

    for port in range(startPort,endPort+1):
        try:
            tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            if not tcp.connect_ex((ip,port)):
                print("[+] TCP open",port)
                tcp.close()
        except Exception:
            pass





def runner():
    socket.setdefaulttimeout(0.01)
    IPAddress = input("enter IP Address: ")
    startPort = int(input("Start Port: "))
    endPort = int(input("End Port: "))
    scanNetwork(IPAddress,startPort,endPort)


runner()
input("Press Enter to close")

