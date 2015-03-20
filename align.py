#! /usr/bin/python

from __future__ import division

import os
import Bio
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
from Bio import Phylo

#use clustalw to generate an alignment

def align_seqs(filename):
    cline = ClustalwCommandline("clustalw2", infile="{}.fasta".format(filename))
    clustalw_exe = r"/users/jnotar/clustalw/clustalw2"
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile="{}.fasta".format(filename))
    assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
    stdout, stderr = clustalw_cline()
    align = AlignIO.read("{}.aln".format(filename), "clustal")

#run the function
align_seqs("echino_sequences")
