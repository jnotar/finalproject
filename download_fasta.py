#This function downloads the content of fasta files from individual identifiers (GI) from genbank
#save the output string as a text file

import Bio #import Biopython
from Bio import Entrez

Entrez.email = "jnotar@ucla.edu" #

#open my idlist from my saved file of GI #s
#idlist = open("genbank_idlist.txt").read()

#this is my test list
idlist = ["47551060", "346418465"] 

def function(list): 
    for id in idlist:
        file = open("{}.txt".format(id), "w")
        handle = Entrez.efetch(db = "nucleotide", id = "{}".format(id), rettype = "fasta", retmode = "text")
        file.write(handle.read())
        file.close()

function(idlist)

print "Done"