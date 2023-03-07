#! /bin/bash  
read -p 'Enter the directory path: ' directory
cd $directory
mkdir secconddirectory
for file in *; do
myfile=$( file $file | grep ASCII | awk '{ print substr( $0, 1, length($0)-12 ) }' | grep a  )
if [[ $myfile == *"txt"* ]]; then
 echo $myfile
mv $myfile . secconddirectory
fi
done
