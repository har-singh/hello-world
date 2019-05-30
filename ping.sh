#!/bin/bash
#---HS 30May19---
#Script to ping the ip address in the list and print result in one line.
#useage: ./ping.sh < list.txt
while read line;
do
echo -ne $line'\t'
ping -c1 -w 2 $line | grep -o '[0-9]*% packet loss'
done
