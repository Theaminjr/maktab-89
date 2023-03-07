#!/bin/bash
read directory
numfolders=`find $directory -maxdepth 1 -type d | wc -l` 
#print only folders
echo $(( $numfolders - 1 ))
#print number of every file except
numfiles=`ls $directory -l | wc -l`
echo $(($numfiles - $numfolders ))
