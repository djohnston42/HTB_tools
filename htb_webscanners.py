import os
import re
import sys


def nikto_scan(htb_ip, htb_name):
    count = 0
    for line in open("/root/Documents/HTB/" + htb_name + "/" + htb_name + ".nmap", "r"):
    #for line in open("/root/Documents/HTB/jerry/jerry.nmap", "r"):
        count + 1
        if "open  http" in line:
            print line
            new = line.split(" ")
            port = new[0]
            port = re.sub('/tcp', '', port)
            print port
            command = ("nikto -h http://" + str(htb_ip) + ":" + str(port) + " > /root/Documents/HTB/" + htb_name + "/" + htb_name + 'nikto' + str(count) + ".txt")
            print command
            os.system(command)

#nikto_scan(htb_ip = "10.10.10.10", htb_name = "jerry")

def dirb_scan(htb_ip, htb_name):
    count = 0 
    for line in open("/root/Documents/HTB/" + htb_name + "/" + htb_name + ".nmap", "r"):
    #for line in open("/root/Documents/HTB/jerry/jerry.nmap", "r"):
        count + 1
        if "open  http" in line:
            print line
            new = line.split(" ")
            port = new[0]
            port = re.sub('/tcp', '', port)
            print port
            command = ("dirb http://" + str(htb_ip) + ":" + str(port) + " > /root/Documents/HTB/" + htb_name + "/" + htb_name + 'dirb' + str(count) + ".txt")
            print command
            os.system(command)

#dirb_scan(htb_ip = '10.10.10.29', htb_name = 'bank')
