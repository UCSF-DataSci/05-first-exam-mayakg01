import random
f = open("bioinformatics_project/data/random_sequence.fasta", "w")
letters = 'ACGT'
fasta_seq = []
fasta_seq = random.choices(letters, k=1000000)
counter = 0
for i in fasta_seq:
    if counter == 80:
        counter = 0
        #set counter to 0 to start a new line for the next 80 bp of the sequence
        f = open("bioinformatics_project/data/random_sequence.fasta", "a")
        f.write("\n")
        #write into file
        f.write(i)
        f.close
        counter += 1
    else:
        f = open("bioinformatics_project/data/random_sequence.fasta", "a")
        f.write(i)
        f.close()
        counter += 1



