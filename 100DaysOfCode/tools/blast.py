#!/local/cluster/bin/python

import os, sys
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio import Seq
from Bio.SeqRecord import SeqRecord


## blast database
nt = "/scratch/zhangya3/proj/16SMicrobial_db/16SMicrobial"
path = "/scratch/zhangya3/proj/single_fa"
target_dir = "/scratch/zhangya3/proj/BLAST_results"
if not os.path.exists(target_dir):
  os.makedirs(target_dir)

files = os.listdir(path)
for file in files:
  file_name = os.path.join(path, file)
  out_file = os.path.join(target_dir, file)
  with open(file_name, "r") as fi, open(out_file, "w+") as fo:
    seq = SeqIO.read(file_name,"fasta")
    result = NcbiblastnCommandline(task="blastn", query="-", db=nt, outfmt=5, evalue=1E-15, out="temp.xml", 
max_target_seqs=100, num_threads=8)
    stdout, stderr = result(stdin=seq.format("fasta"))
    record = open("temp.xml")
    blast_record = NCBIXML.read(record)
    record.close()
    for alignment in blast_record.alignments:
      for hsp in alignment.hsps:
        title_element = alignment.title.split()
        print alignment.accession
	fo.write(">"+title_element[1]+" "+title_element[2]+" "+title_element[3]+" "+title_element[4]+"\n"+hsp.sbjct+"\n")

print('\x1b[6;30;42m' + '>> ALL Done!' + '\x1b[0m')
