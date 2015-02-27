#! /usr/bin/python

from __future__ import division

#This function downloads the content of fasta files from individual identifiers (GI) from genbank
#save the output string as a text file

#Import important packages: regex, Biopython, & Entrez (from Biopy)
import re
import Bio
from Bio import Entrez

Entrez.email = "jnotar@ucla.edu" #tell Entrez who you are

def download_fasta(org, gene): 
	#open my idlist from my saved file of GI #s
    idlist = open("{}_{}_ids.txt".format(org, gene)).read() #open list & read into one string 
    idlist = re.findall(r"\'(\d+)\'", idlist) #get rid of other characters by cutting out each id and putting it in a separate entry in a list
    for id in idlist:
        file = open("{}.fasta".format(id), "w")
        	#change "{}.fasta" to "{}.txt" if you want to save it as a text file. But why? 
        handle = Entrez.efetch(db = "nucleotide", id = "{}".format(id), rettype = "fasta", retmode = "text")
        	#tell Entrez to fetch entries from nucleotide, that match id from idlist, fasta files only
        file.write(handle.read()) #write to file object
        file.close() #close file

download_fasta("Echinodermata", "opsin") #run the function on the idlist of GIs

print "Done"