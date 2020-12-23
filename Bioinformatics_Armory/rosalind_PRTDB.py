import os
import sys
from Bio import ExPASy
from Bio import SwissProt

f1 = sys.argv[1]
protein_list = []
with open(f1,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        protein_list.append(line)
'''
#os.mkdir(os.getcwd() +'/prt_db')

os.chdir(os.getcwd() + '/prt_db')
print(os.getcwd())
for i in protein_list:
    os.system('wget http://www.uniprot.org/uniprot/{}.txt'.format(i))


file_list = os.listdir(os.getcwd())

prt_db = []
for i in file_list:
    with open(i,'r') as handle:
        for lines in handle:
            line = lines.split('.')
            for j in line:
                if j.find('P:') >= 0:
                    a = j.split(';')
'''
for i in protein_list:
    handle = ExPASy.get_sprot_raw(i)
    record = SwissProt.read(handle)
    for j in record.cross_references:
        for k in j:
            if k.startswith('P:'):
                print(k.lstrip('P:'))
