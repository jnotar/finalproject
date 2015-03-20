#! /usr/bin/python

from __future__ import division

#This converts a all the fasta files in a folder into a single file
    #can specify the type of file in (e.g. fasta), and the type of file out (e.g. nexus or fasta)

import Bio
import glob

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein

def single_file(filename, filein, fileout):
    #filename = what you want the file to be called
    #filein = type of file you're putting in
    #fileout = what type of file you want out
    list = [] #initiate a list
    #use glob to get all files in a folder
    files = glob.glob("*.{}".format(filein)) #grabs all gb files in a folder
    #Parse each gb file
    for file in files: 
        #open the file
        record = SeqIO.read("{}".format(file), "{}".format(filein))
        #append to list
        list.append(record)
    #write the list as a single file, specify type
    SeqIO.write(list, "{}.{}".format(filename, fileout), "{}".format(fileout))

single_file("echino_sequences", "fasta", "fasta")





