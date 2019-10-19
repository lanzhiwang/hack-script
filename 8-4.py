from _winreg import *
import sys

varSubKey = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"                #(1)
varReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)                                   #(2)
varKey = OpenKey(varReg, varSubKey)                                                        #(3)
for i in range(1024):                                           
    try:
        keyname = EnumKey(varKey, i)                                                        #(4)
        varSubKey2 = "%s\\%s"%(varSubKey,keyname)                                       #(5)
        varKey2 = OpenKey(varReg, varSubKey2)                                             #(6)
        try:
            for j in range(1024):
                n,v,t = EnumValue(varKey2,j)                                                   #(7)
                if("ProfileImagePath" in n and "Users" in v):                                  #(8)
                    print v
        except:
            errorMsg = "Exception Inner:", sys.exc_info()[0]
            #print errorMsg
        CloseKey(varKey2)
    except:                                               
        errorMsg = "Exception Outter:", sys.exc_info()[0]
        break          
CloseKey(varKey)                                                                                 #(9)
CloseKey(varReg)
