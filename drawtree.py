#! /usr/bin/python

from __future__ import division

import Bio
import sys
import os
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
from Bio import Phylo

#Function that draws an ascii tree in python
def draw_tree_inline(filename):
	tree = Phylo.read("{}.dnd".format(filename), "newick")
	Phylo.draw_ascii(tree)

#Function that draws picture file of a tree w/ matplot lib
def draw_tree_png(filename):
    tree = Phylo.read("{}.dnd".format(filename), "newick") #read the tree from the dnd file
    tree.rooted = True
    Phylo.draw(tree) #if we want to see the tree drawn
    Phylo.write(tree, "{}.nwk".format(filename), "newick") #save file as a newick tree

#run it for my echino sequences
draw_tree_png("echino_sequences")
