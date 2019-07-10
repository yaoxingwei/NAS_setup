#!/bin/sh

basepath=$(cd `dirname $0`; pwd)

case $1 in
start)
	aria2c --conf-path=$basepath/aria2_yxw.conf -D
	;;
stop)
	killall -9 aria2c
	;;
restart)
	killall -9 aria2c
	sleep 1
	aria2c --conf-path=$basepath/aria2_yxw.conf -D
	;;
esac
