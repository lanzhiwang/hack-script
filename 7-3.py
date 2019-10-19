from ftplib import FTP

apacheDir = "htdocs"
serverName = "server"
serverID = "server"
serverPW = "server"

def getDirList(cftp, name):                            #(1)
    dirList = []
    if("." not in name):                               #(2)
        if(len(name) == 0):
            dirList = ftp.nlst()                       #(3)
        else:
            dirList = ftp.nlst(name)               
    return dirList

def checkApache(dirName1, dirName2):                   #(4)
    if(dirName1.lower().find(apacheDir) >= 0):             
        print dirName1
    if(dirName2.lower().find(apacheDir) >= 0):
        print dirName1 +"/"+ dirName2

ftp = FTP(serverName, serverID, serverPW)              #(5)

dirList1 = getDirList(ftp, "")                         #(6)

for name1 in dirList1:                                 #(7)
    checkApache(name1,"")                              #(8)
    dirList2 = getDirList(ftp, name1)                  #(9)
    for name2 in dirList2:
        checkApache(name1, name2)
        dirList3 = getDirList(ftp, name1+"/"+name2)
