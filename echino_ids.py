#! /usr/bin/python

from __future__ import division

#Get a list of IDs for all Echinoderm + opsin search queries on GenBank
	#This is for DNA, not proteins >> necessary if we're going to compare % nucleotide similarity later

#Import important packages: regex, Biopython, & Entrez (from Biopy)
import re 
import Bio
from Bio import Entrez

Entrez.email = "jnotar@ucla.edu" #tell NCBI who you are

#search Organism: Echinodermata AND Title contains "opsin"
handle = Entrez.esearch(db = "nucleotide", term = "Echinodermata[Orgn] AND opsin[Titl]")
record = Entrez.read(handle)
#if we did: record["Count"] 
	#We get 22 results from this
ids = record["IdList"]

#if we want to save it to a file
echino_ids = open("echino_ids.txt", "w")
echino_ids.write(str(ids)) #this saves it as a literal string... enh, less than optimal, but works if we do the workaround in the next step
echino_ids.close()