#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Windows 缓冲区溢出

基于 SHE 的缓冲区溢出

以 Adrenalin https://www.exploit-db.com/exploits/26525 应用为例

"""

from pydbg import *
from pydbg.defines import *
import struct
import utils

processName = "Play.exe"

dbg = pydbg()


def handler_av(dbg):
    crash_bin = utils.crash_binning.crash_binning()
    crash_bin.record_crash(dbg)
    print crash_bin.crash_synopsis()

    dbg.terminate_process()


for (pid, name) in dbg.enumerate_processes():
    if name == processName:
        print "[information] dbg attach:" + processName
        dbg.attach(pid)

print "[information] start dbg"
dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, handler_av)
dbg.run()
