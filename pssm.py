#this is a sh and python script for creating:
# - Frequency matrix
# - Position-specific scoring matrix

# download reference genome and unzip reference genome
#wget -q -O ref.fa.gz ftp://ftp.ensemblgenomes.org/pub/bacteria/release-37/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz

#unzip reference genome
#gunzip -c ref.fa.gz > ref.fa

# import division function for calc background probabilities
from __future__ import division

#import log function
import math

# calc background probabilities
reference=open('/Users/tennisluver/Documents/GitHub/python/sampleref.fa')
refstr=''
for line in reference:
    if line[0]!='>':
        line=line.strip()
        refstr=line
A_count = [x for x in refstr if x=='A']
T_count = [x for x in refstr if x=='T']
C_count = [x for x in refstr if x=='C']
G_count = [x for x in refstr if x=='G']
a=len(A_count)
t=len(T_count)
c=len(C_count)
g=len(G_count)
total=len(refstr)
propa=a/total
propt=t/total
propc=c/total
propg=g/total
print propa, propt, propc, propg

#open alignment file
alignment=open('/Users/tennisluver/Documents/GitHub/python/sample.fa')
text=[]
#for the alignment file, do not read lines containing >sequence name
# line=line.strip() removes "\n" from the end of the line (python formatting)
for line in alignment:
    if line[0]!='>':
        line=line.strip()
        text.append(line)

# alignment matrix
# "x" is treated as a character for A, T, C, and G
r = 10 #because there are 10 sequences
m = []
for i in range(r):
    m.append([x for x in text[i]])
for i in m:
    print (i)
print (m)

# extract column from matrix
def column(matrix, i):
    return [row[i] for row in matrix]

#To check the function use:
#print column(m,0)

# frequency matrix
# for each column, count the number of NTs
fmatrix=[]
r = 12 #because there are 12 NTs per sequence
for i in range(r):
    a=column(m,i)
    fmatrix.append(a)
print (fmatrix)

# count NTs in each column
# "len" counts elements in a list
f2matrix=[]
pmatrix=[]
p2matrix=[]
for row in fmatrix:
    A_list = [x for x in row if x=='A']
    T_list = [x for x in row if x=='T']
    C_list = [x for x in row if x=='C']
    G_list = [x for x in row if x=='G']
    a=len(A_list)
    t=len(T_list)
    c=len(C_list)
    g=len(G_list)

# add pseudocount to remove zeros from fmatrix
    f2matrix.append([a+0.25, t+0.25, c+0.25, g+0.25])
# calculate probability matrix
    pmatrix.append([(a+0.25)/13, (t+0.25)/13, (c+0.25)/13, (g+0.25)/13])
# create PSSM using log2(p/q)
# p2matrix = PSSM
    p2matrix.append([math.log(((a+0.25)/13)/propa,2), math.log(((t+0.25)/13)/propt,2), math.log(((c+0.25)/13)/propc,2), math.log(((t+0.25)/13)/propt,2)])
print (f2matrix)
print (pmatrix)
print (p2matrix)
