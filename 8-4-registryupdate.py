#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""创建和修改注册表信息"""

from _winreg import *
import sys

varSubKey = "SYSTEM\CurrentControlSet\services\SharedAccess\Parameters\FirewallPolicy"
varStd = "\StandardProfile"
varPub = "\PublicProfile"
varEnbKey = "EnableFirewall"
varOff = 0

try:
    varReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

    varKey = CreateKey(varReg, varSubKey+varStd)
    SetValueEx(varKey, varEnbKey, varOff, REG_DWORD, varOff)
    CloseKey(varKey)

    varKey = CreateKey(varReg, varSubKey+varPub)
    SetValueEx(varKey, varEnbKey, varOff, REG_DWORD, varOff)

except Exception:
    errorMsg = "Exception Outter:", sys.exc_info()[0]
    print errorMsg

CloseKey(varKey)
CloseKey(varReg)
