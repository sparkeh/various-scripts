#!/bin/bash

if [ -z "$1" ]
  then
    watch -n3 ./check-ips.sh    
  else
    watch -n$1 ./check-ips.sh
fi
