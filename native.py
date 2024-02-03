from scapy.all import *

def find_vlan(packet, vln_tar):
    for layer in packet:
        if isinstance(layer, Dot1Q):
            if layer.vlan == vln_tar:
                return True
    return False

def main():
    ip = input("Enter the target ip: ")
    vlan = 1
    lan = False
    packet = Ether(dst= 'ff:ff:ff:ff:ff:ff') / Dot1Q(vlan= vlan) / IP(dst= ip)
    
    answer = sr1(packet, timeout=0.5, retry=1)
    
    if answer is None:
        print("The ip in a LAN!")
        lan = True
    else:
        while not find_vlan(answer, ip):
            print(f"The {vlan} is not the vlan")
            vlan += 1 
if __name__ == '__main__':
    main()
