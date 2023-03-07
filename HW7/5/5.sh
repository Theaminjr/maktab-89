#! /bin/bash  
read directory  #example /home/amin/Desktop/test
if [ -d "$directory" ]; then
echo "directory already exists"
else 
echo "directory did not exist. it is created now"
mkdir $directory
fi
