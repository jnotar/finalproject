#! /usr/bin/python

from __future__ import division

#This function downloads the content of fasta files from individual identifiers (GI) from genbank
#save the output string as a text file

#Import important packages: regex, Biopython, & Entrez (from Biopy)
import re
import Bio
from Bio import Entrez

Entrez.email = "jnotar@ucla.edu" #tell Entrez who you are

def download_files(org, gene, filetype): 
	#open my idlist from my saved file of GI #s
    idlist = open("{}_{}_ids.txt".format(org, gene)).read() #open list & read into one string 
    idlist = re.findall(r"\'(\d+)\'", idlist) #get rid of other characters by cutting out each id and putting it in a separate entry in a list
    for id in idlist:
        file = open("{}.{}".format(id, filetype), "w")
        	#change "{}.fasta" to "{}.txt" if you want to save it as a text file. But why? 
        handle = Entrez.efetch(db = "nucleotide", id = "{}".format(id), rettype = "{}".format(filetype), retmode = "text")
        	#tell Entrez to fetch entries from nucleotide, that match id from idlist, correct filetype
        file.write(handle.read()) #write to file object
        file.close() #close file

download_files("Echinodermata", "opsin", "fasta") #run the function on the idlist of GIs for fasta files

print "Done"