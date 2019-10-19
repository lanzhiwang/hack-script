#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""将后门客户端编译成 Windows 可执行的 exe 文件"""

from distutils.core import setup
import py2exe

options = {
	"bundle_files": 1,
	"compressed": 1,
	"optimize": 2
}

setup(
	console=["8-1-backdoorclient.py"],
	options={"py2exe": options},
	zipfile=None
)

# python -u 8-3-setup.py py2exe
