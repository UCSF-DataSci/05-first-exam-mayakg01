### Description of Bioinformatics Project
## We have 3 subdirectories within our bioinformatics project directory
## Data Subdirectory
-**random_sequence.fasta**: a text file containing a randomly generated DNA sequence of 1 million DNA nucleotides
## Results Subdirectory
-**cutsite_summary.txt**: a text file containing a summary of the results of using the "find_cutsites.py" script to find pairs of restriction enzyme cut sites that are 80-120 kbp apart in the random fasta file
## Scripts Subdirectory
- **dna_operations.py**: This script writes three functions that will be carried out on a random DNA sequence: complement (finding the complement of the DNA sequence), reverse, and reverse complement
- **find_cutsites.py**: This script takes in the random fasta file: "random_sequence.fasta" located in the data subdirectory and and the cutsite "G|GATCC" as input and saves a summary of the results to the text file "cutsite_summary.txt"
- **generate_fasta.py**: This script generates a random fasta file containing a randomly generated DNA sequence (comprised of the nucleotides A, T, G, C) that is 1 million base pairs in length
