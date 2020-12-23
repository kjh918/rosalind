import sys
from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
f = sys.argv[1]

gene_set = ''
with open(f,'r') as handle:
    for i in handle:
        gene_set += i.replace('\n','')

gene_s = gene_set.split(' ' )
Entrez.email = 'pj02146@gmail.com'
x = []
handle = Entrez.efetch(db="nucleotide",id=gene_set,rettype='fasta')
records = list(SeqIO.parse(handle,'fasta'))

for i in range(len(records)):
    x.append(len(records[i].seq))

print(x)
print(min(x))
print(gene_set[0])

for i in range(len(x)):
    if min(x) == x[i]:
        handle = Entrez.efetch(db="nucleotide",id=[gene_s[i]],rettype='fasta')
        records = handle.read()
        print(records)
