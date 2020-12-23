import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

f = sys.argv[1]

seq = SeqIO.parse(f,'fasta')

seq_list = []
rev_seq = []
for i in seq:
    seq_list.append(str(i.seq))
    rev_seq.append(str(i.seq.reverse_complement()))

count = 0
for i in range(len(seq_list)):
    print(seq_list[i])
    print(rev_seq[i])
    if str(seq_list[i]) == str(rev_seq[i]):
        count += 1

print(count)
