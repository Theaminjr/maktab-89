#! /bin/bash
echo "enter url"  
read URL
wget $URL
touch log.txt
echo $URL > log.txt
