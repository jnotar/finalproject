#! /bin/bash

#uses awk program to take line breaks/wraps out of fasta file
awk '/^>/{print s? s"\n"$0:$0;s="";next}{s=s sprintf("%s",$0)}END{if(s)print s}' echino_sequences.fasta > new.fasta

#rewrites improved stuff to original file for ease of file names
cat new.fasta > echino_sequences.fasta

#remove temporary file
rm new.fasta
