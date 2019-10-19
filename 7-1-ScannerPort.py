#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""利用 nmap 工具实现端口扫描"""

import sys
import os
import socket
import nmap

nm = nmap.PortScanner()
nm.scan('server', '1-1024')

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : {0} ({1})'.format(host, nm[host].hostname()))
    print('State : {0}'.format(nm[host].state()))

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}'.format(proto))

        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))

print('----------------------------------------------------')
