 #-d to choose a directory
 #-F to choose file format
 #-f to choose only one file


import argparse
import os
from color import *

parser = argparse.ArgumentParser(
         prog = 'FileSizer',
         description = 'get size of the files recursively'
)


parser.add_argument("-d",help="a directory to search recursively",nargs=1)
parser.add_argument("-f",help="choose only one file to get size of",nargs=1)
parser.add_argument("-F",help="choose a file format, should be used by -d",nargs=1)
args = parser.parse_args()



def find_names_in_directory(to_check:list,allpaths:list): # recurcive function to get all paths available in a directory
   for path in to_check:
      try:
         names = os.listdir(path)
      except NotADirectoryError:
         names = None
      to_check.remove(path)
      allpaths.append(path)
      if names:
         for name in names:
            to_check.append(f"{path}/{name}")

   if len(to_check)== 0:
      return allpaths
   else:
      return find_names_in_directory(to_check, allpaths)


if args.d and args.F and args.f == None:
   total = 0
   all_paths = find_names_in_directory([args.d],[])
   for path in all_paths:
       if args.F in path:
         size = os.path.getsize(path)
         total+=size
         print(f"{path} ==> kb:" ,end="")
         print_OKGREEN(size/1000)
   print("total ==> " ,end="")
   print_FAIL(total)
elif args.d and args.F == None and args.f == None:
   total = 0
   all_paths = find_names_in_directory([args.d],[])
   for path in all_paths:
      size = os.path.getsize(path)
      total += size
      print(f"{path} ==> kb:" ,end="")
      print_OKGREEN(size/1000)
   print("total ==> " ,end="")
   print_FAIL(total)
elif args.d == None and args.F == None and args.f:
   size = os.path.getsize(args.f)
   print(f"{args.f} ==> kb:" ,end="")
   print_OKGREEN(size/1000)
else:
   print_FAIL("you chosed a wrong combination of commands , correct cobinations are : (-d)(-d -F)(-f)")


   


