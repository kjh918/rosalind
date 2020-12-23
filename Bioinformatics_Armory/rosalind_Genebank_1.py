import sys
from Bio import Entrez

f = sys.argv[1]

data = []
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        data.append(line)

print(data)
Entrez.email = 'pj02146@gmail.com'


handle = Entrez.esearch(db='nucleotide',term = '("{0}"[Organism]) AND ("{1}"[Publication Date] : "{2}"[Publication Date]")'.format(data[0],data[1],data[2]))
record = Entrez.read(handle)
print(record)
print(record['Count'])

geneName = data[0]
pubDateStart = data[1]
pubDateEnd = data[2]
searchTerm = f'({geneName}[Organism]) AND("{pubDateStart}"[Publication Date]: "{pubDateEnd}"[Publication Date])'

print(f"\n[GenBank gene database]:")
handle = Entrez.esearch(db="nucleotide", term=searchTerm)
record = Entrez.read(handle)
print(record)
print(record["Count"])

