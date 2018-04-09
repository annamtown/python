#this is a sh and python script for creating:
# - Frequency or probability matrix
# - PSSM
# - Scores for all motif sequences in the input alignment
# - List of all positions in the analyzed sequence with score less than or equal to zero
#       - For each motif occurrence, list position (start-end), actual sequence, and score


# download reference genome and unzip reference genome
wget -q -O ref.fa.gz ftp://ftp.ensemblgenomes.org/pub/bacteria/release-37/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz

#unzip reference genome
gunzip -c ref.fa.gz > ref.fa


#start python

python

# call sample.fa file

alignment=open(/Users/tennisluver/Documents/GitHub/python/sample.fa)

# create frequency matrix


text = [[print(seq0)][print(seq1)][print(seq2)][print(seq3)][print(seq4)][print(seq5)][print(seq6)][print(seq7)][print(seq8)][print(seq9)]
r = 10 #because there are 10 sequences
m = []
for i in range(r):
    m.append([int(x) for x in text[i]])
for i in m:
    print (i)


# Adjust frequency matrix


# Construct probability matrix based on background NT probabilities (GC content)
