#! /usr/bin/python

from __future__ import division

#Get a list of IDs for all <Organism name> + <word in title aka gene> search queries on GenBank
	#Searching nucleotide, not protein

#Import important packages: regex, Biopython, & Entrez (from Biopy)
import re 
import Bio
from Bio import Entrez

Entrez.email = "jnotar@ucla.edu" #tell NCBI who you are

def get_gb_ids(org, gene): #function searches "org" and "gene in title"
    handle = Entrez.esearch(db = "nucleotide", term = "{}[Orgn] AND {}[Titl]".format(org, gene))
    record = Entrez.read(handle)
    ids = record["IdList"]
	#save list of ids to a file
    entry_ids = open("{}_{}_ids.txt".format(org, gene), "w")
    entry_ids.write(str(ids)) #this saves it as a literal string... enh, less than optimal, but works if we do the workaround when opening it (see comments below "print")
    entry_ids.close()

#Call function
get_gb_ids("Echinodermata", "opsin")

print "Done!"

#######
#This is how we work around the our id list being a literal string
	#since likely we want to open it and have each id be an entry in a list in python
#idlist = open("echino_ids.txt").read() #open list & read into one string 
#idlist = re.findall(r"\'(\d+)\'", idlist) #get rid of other characters by cutting out each id and putting it in a separate entry in a list









