# Python 黑客攻防入门脚本

* [tcp 代理脚本](./tcp-proxy.sh)
* [键盘钩取，获取键盘输入](./5-1-MessageHooking.py)
* [利用 nmap 工具实现端口扫描](./7-1-ScannerPort.py)
* [破解 ftp 服务密码](./7-2-CrackPasswords.py)
* [访问 ftp 服务目录列表](./7-3-DirList.py)
* [ftp web shell 攻击](./7-4-WebShell.py)
* [内网包嗅探技术](./7-5-Sniffing.py)
* 后门攻击
	* [后门服务端](./8-1-backdoorserver.py)
	* [后门客户端](./8-1-backdoorclient.py)
	* [将后门客户端编译成 Windows 可执行的 exe 文件](./8-1-setup.py)
* 注册表
	* [访问注册表信息息](./8-4-registrylist.py)
	* [创建和修改注册表信息](./8-4-registryupdate.py)
* Windows 缓冲区溢出
	* 基于栈的缓冲区溢出
		* [step 1](./8-6-1.py)
		* [step 2](./8-6-2.py)
		* [step 3](./8-6-3.py)
		* [step 4](./8-6-4.py)
		* [step 5](./8-6-5.py)
	* 基于 SHE 的缓冲区溢出
		* [step 1](./8-12-1.py)
		* [step 2](./8-12-2.py)
		* [step 3](./8-12-3.py)
		* [step 4](./8-12-4.py)


# 常见的 DoS 攻击技术：

## 利用 ICMP 协议

* **[死亡之 ping (Ping of Death)](./7-6-Dos-ping.py)**

ping 实用程序使用的 ICMP 包很大(如 65535 字节)，远远大于普通大小(32 字节)时，他就会被分片，分割为网络可以处理的大小。服务器处理大量 ICMP 包时会消耗大量的系统资源，最终资源耗尽，导致瘫痪。

* **Smurf Attack**

该攻击恶意利用 ICMP 包特性。ICMP 协议的特征是，发送请求就会有响应。发送 ICMP 请求前，先将 ICMP 包源地址更改为目标服务器地址。这样，每个收到 ICMP 请求的主机都会做出答复，导致服务器被大量的 ICMP 响应吞没，网络发送阻塞，从而拒接为正常请求服务。

## 利用 TCP 协议

* **[TCP SYN 洪水攻击](./7-7-Dos-TCPSYN.py)**

该攻击利用了 TCP 连接过程中的安全缺陷。客户机向服务器发送 SYN 包时，服务器会向客户机回送 SYN/ACK 包。然后，客户机向服务器发送 ACK 包建立 TCP 连接。若最后一步客户机不向服务器发送 ACK 包，则服务器一直等待，处于 SYN Received 状态。不断重复这一过程，服务器的缓冲(半连接队列)将被全部耗尽，从而瘫痪。

* **着陆攻击 (Land Attack)**

请求 TCP 连接发送 SYN 包时，SYN 包具有相同的源地址和目的地址，均设置为服务器地址。这样，服务器回送 SYN/ACK 包时，发现目的地址就是自己，导致服务器不断向自己发送 SYN/ACK 包，最终导致系统奔溃。

## 利用 HTTP 协议

* **[Slowloris Attack](./7-8-Dos-slowloris.py)**

黑客与服务器建立正常回话后，向服务器发送非正常的 HTTP 请求头(未结束的 HTTP 请求头)。服务器认为 HTTP 请求头部分没有结束，保持此连接不释放，继续等待完整请求。随着这种开放状态的连接数不断增加，服务器的连接数就会很快达到上限，从而无法处理新的请求。

* **HTTP 洪水攻击**

该攻击大量调用正常服务，使服务瘫痪。若同时大量请求 WEB 服务器提供服务的 URL，WEB 服务器的 CPU 和连接资源会很快耗尽，从而陷于瘫痪。

## 其他

* **Tear Drop 攻击**

传送大数据包时，会先对数据包进行分片。这些分片到达目的地时会重新组装。分片数据包包含该分片的偏移量，可以通过操纵偏移量的值，使其大于实际的偏移量，造成重叠偏移。这会引发服务器溢出的问题，使服务陷于瘫痪。

# 常见工具

* Scapy

# 参考

* [/geekcomputers/Python](https://github.com/geekcomputers/Python)
