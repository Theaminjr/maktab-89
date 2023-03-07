#! /bin/bash  
read directory
cd $directory
touch merge.txt
cat *.txt >> merge.txt 
sed -n 5,10p merge.txt
