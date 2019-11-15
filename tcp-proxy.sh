#!/bin/sh -e

# https://www.kawabangga.com/posts/3723
# https://notes.tweakblogs.net/blog/7955/using-netcat-to-build-a-simple-tcp-proxy-in-linux.html

set -x

if [ $# != 3 ]
then
    echo "usage: $0 <src-port> <dst-host> <dst-port>"
    exit 0
fi

TMP=`mktemp -d`  # /tmp/tmp.GU3zsslTMm
BACK=$TMP/pipe.back  # /tmp/tmp.GU3zsslTMm/pipe.back
SENT=$TMP/pipe.sent  # /tmp/tmp.GU3zsslTMm/pipe.sent
RCVD=$TMP/pipe.rcvd  # /tmp/tmp.GU3zsslTMm/pipe.rcvd
trap 'rm -rf "$TMP"' EXIT  # rm -rf /tmp/tmp.GU3zsslTMm
mkfifo -m 0600 "$BACK" "$SENT" "$RCVD"  # mkfifo -m 0600 /tmp/tmp.GU3zsslTMm/pipe.back /tmp/tmp.GU3zsslTMm/pipe.sent /tmp/tmp.GU3zsslTMm/pipe.rcvd
sed 's/^/ => /' <"$SENT" &
sed 's/^/<=  /' <"$RCVD" &
nc -l -p "$1" <"$BACK" | tee "$SENT" | nc "$2" "$3" | tee "$RCVD" >"$BACK"

# ./tcp_proxy.sh 8800 127.0.0.1 6379
# redis-cli -p 8800

# ./tcp_proxy.sh 8800 baidu.com 80
# curl --proxy 127.0.0.1:8800 baidu.com -v