#!/bin/bash
##-----HS 30May19-----
#Script to ping the ip address in the list and print result in one line.
#useage: ./ping.sh < list.txt


# HS 06May21
# https://stackoverflow.com/questions/18123211/checking-host-availability-by-using-ping-in-bash-scripts
# https://unix.stackexchange.com/questions/3747/understanding-the-exclamation-mark-in-bash
# https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux

RED='\033[0;31m'
NC='\033[0m' # No Color
#printf "Color ${RED}red${NC} Thanks Stack Overflow\n"

while read line;
do
  if ping -c1 -w 2 $line &> /dev/null
  then
    printf "${RED}${line}\tNOK${NC}\n" # exit code 1
  else
    printf "${line}\tOK\n" # exit code 0
  fi
done
