#! /bin/python

#This script takes that massive, unformatted list of genus names, cuts them out, and puts them on separate lines of a new text file

#import regular expressions
import re

#create the file we want to write to
final_list = open("genus_list.txt", "w")
#open & read the terrible text file
genus_list = open("echinoid_genuses.txt").read()

#substitute all genus names with "Genus\n"
list = re.sub(r"([A-Za-z]{2,30})\s", r"\1\n", genus_list) 

#Find all Genus names and put them in a list
list = re.findall(r"([A-Za-z]{2,30}\n)", list)

#Write all lines of the list to our file object
final_list.writelines(list)

#Close the file object
final_list.close()
