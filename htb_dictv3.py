import os
import re
import sys
import nmap
from htb_webscanners import *

htb_dict = {

	'nibbles': '10.10.10.75',
	'tenten': '10.10.10.10',
        'localhost': '127.0.0.10',
        'legacy': '10.10.10.4'
}

nmap_dict = {
        '1': 'nmap -sC -sV -oA',
        '2': 'nmap -sC -sV -p- -oA',
        '3': 'nmap -sC -sV -p- --max-rtt 1000ms -oA'
}

def main():
        append_boxes()
	list_boxes()
	box_name = raw_input("choose box:  ")
	box_IP = htb_dict.get(box_name)
	print box_IP
	if box_IP == 'none':
		print 'enter valid box name'
	else:
            if host_status(box_IP):
                path_root = ("/root/Documents/HTB/" + box_name)
                make_dir(path_root)
                scan(box_name, box_IP, path_root)
                nikto_scan(box_IP, box_name)
            else:
                print 'host not online'

def host_status(host):
    box_status = False
    if os.system("ping -c 1 " + host) == 0:
        box_staus = True
        return True
    else:
        box_status = False
        return False

def scan(name, ip, path_root):
    scan_type = 0
    scan_type = raw_input("select scan level:  ")
    set_scan = nmap_dict.get(scan_type)
    print set_scan
    scan_str = (str(set_scan) + " " + path_root + "/" + name + " " + ip)
    print scan_str
    os.system(scan_str)

def make_dir(path_root):
    try:
        os.makedirs(path_root)
    except OSError:
        if  not os.path.isdir(path_root):
            raise

def append_boxes():
    new_boxname = raw_input("Input new Box name:  ")
    new_boxIP = raw_input("Input new Box IP:  ")
    htb_dict[new_boxname] = new_boxIP

def list_boxes():
	for key in htb_dict:
		print key, ':', htb_dict[key]
		

main()
