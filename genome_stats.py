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
feature_types = {} # keeps track of the counts of all feature types

total_feature_count = 0

feature_lengths = {} # keeps track of the lengths of all feature types
protein_coding_length = 0 # computed total of all protein coding gene lengths
debug = False
with open(gff,"r") as fh:
    # now add code to process this
    gff = csv.reader(fh,delimiter="\t")
    i = 0
    for row in gff:
        if row[0].startswith("#"): 
            # skip comment / header lines
            continue
        # example of printing out some of the data in the file
        ftype = row[2]
        if ftype not in feature_types: # counting up feature type abundance
            feature_types[ftype] = 0 # if this is first time for the feature, set the counter to 0
        feature_types[ftype] += 1 # add 1 to the counts for this feature type ('ftype')
        total_feature_count += 1 # count up the TOTAL number of features in the file

        feature_length = abs(int(row[4]) - int(row[3])) + 1 # compute the length of the feature (we add 1 because the feature start at 1)
        if ftype == "protein_coding_gene": # if it is a protein coding gene 
            protein_coding_length += feature_length # add this length to a specific counter variable

        # count up the length of all features
        if ftype not in feature_lengths: # if this feature type is not in the dictionary 
            feature_lengths[ftype] = 0 # set its length to 0
        feature_lengths[ftype] += feature_length # add lengths up by feature type

        # debugging code to stop after 10 lines of features
        if debug:
            print(row[0],row[2],row[3],row[4],row[6])
            print("feature length is {}".format(feature_length))
            if i > 10:
                break
        i += 1

print("The types and abundances of features are:")
for type in feature_types:
    print("Feature %s is found %d which is %.2f%% of the features"%(type,feature_types[type], 100 * (feature_types[type]/total_feature_count)))

print("Total protein coding lengths are: {}".format(protein_coding_length))
for type in feature_lengths:
    print("Feature %s lengths total is %d"%(type,feature_lengths[type]))

genome_len = 0 # this is the counter variable for the total length of the genome (sum of the lengths of all the sequences)
# open the FASTA file and read it witjh the aspairs() function
with open(fasta,"r") as f:
    seqs = dict(aspairs(f)) # get back a dictionary for the fasta file, where keys are the names of contigs and values are the sequence data as a string
    print("there are", len(seqs.keys()),"contigs")
    for seqid in seqs: # loop through all the sequences in the file
        seqstring = seqs[seqid]

        genome_len += len(seqstring)
    #   for seqid in seqs.keys():
#       print("seqname is",seqid)

print("Genome length is {} basepairs".format(genome_len))

print("Percent of the genome which is protein_coding_gene = %.2f%%"%(100 * protein_coding_length / genome_len))
for type in feature_lengths:
    print("Feature %s lengths percentage of genome is %.2f%%"%(type,100 * feature_lengths[type] / genome_len))