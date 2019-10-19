import os

def makeFile(fileName, message, mode):                        #(1)
    a=open(fileName, mode)                                    #(2)
    a.write(message)                                          #(3)
    a.close()                                                 #(4)

def openFile(fileName):                                       #(5)
    b=open(fileName, "r")                                     #(6)
    lines = b.readlines()                                     #(7)
    for line in lines:                                        #(8)
        print(line)
    b.close()

makeFile("fileFirst.txt","This is my first file1\n","w")      #(9)
makeFile("fileFirst.txt","This is my first file2\n","w")  
makeFile("fileFirst.txt","This is my first file3\n","w")  
makeFile("fileSecond.txt","This is my second file 1\n","a")   #(10)
makeFile("fileSecond.txt","This is my second file 2\n","a")
makeFile("fileSecond.txt","This is my second file 3\n","a")


print("write fileFirst.txt")
print("-----------------------------")
openFile("fileFirst.txt")                                     #(11)
print("-----------------------------")

print("\n")

print("write secondFirst.txt")
print("-----------------------------")
openFile("fileSecond.txt")                                    #(12)
print("-----------------------------")
