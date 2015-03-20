#! /usr/bin/python

from __future__ import division

import Bio
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
	tree = Phylo.read("{}.dnd".format(filename), "newick")
	tree.rooted = True
	Phylo.draw(tree)

#run it for my echino sequences
draw_tree_png("echino_sequences")