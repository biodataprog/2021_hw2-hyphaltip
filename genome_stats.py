#!/usr/bin/env python3
#!/usr/bin/env python3

# this is a python script template
# this next line will download the file using curl

import os,itertools,csv,re

gffurl="https://fungidb.org/common/downloads/release-54/PchrysosporiumRP-78/gff/data/FungiDB-54_PchrysosporiumRP-78.gff"
gff=os.path.basename(gffurl)
fastaurl="https://fungidb.org/common/downloads/release-54/PchrysosporiumRP-78/fasta/data/FungiDB-54_PchrysosporiumRP-78_Genome.fasta"
fasta=os.path.basename(fastaurl)


# this is code which will parse FASTA files
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence


if not os.path.exists(gff):
    os.system("curl -O {}".format(gffurl))

if not os.path.exists(fasta):
    os.system("curl -O {}".format(fastaurl))

# open the GFF file, use the csv module, and write code to compute statistics
with open(gff,"r") as fh:
    # now add code to process this
    gff = csv.reader(fh,delimiter="\t")
    for row in gff:
        if row[0].startswith("#"):
            continue
        # example of printing out some of the data in the file
#        print(row[0],row[2],row[3],row[4],row[6])

genome_len = 0
# open the FASTA file and read it witjh the aspairs() function
with open(fasta,"r") as f:
   seqs = dict(aspairs(f))
   print("there are", len(seqs.keys()),"contigs")
   for seqid in seqs.keys():
       print("seqname is",seqid)

print("Genome length is {} basepairs".format(genome_len))
