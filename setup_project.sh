#!/bin/bash
chmod +x setup_project.sh
#part 1
mkdir bioinformatics_project
# part 2: creating subdirectories
cd /workspaces/05-first-exam-mayakg01/bioinformatics_project
mkdir data
mkdir scripts
mkdir results
#part 3: creating empty python files
cd /workspaces/05-first-exam-mayakg01/bioinformatics_project/scripts
touch generate_fasta.py
touch dna_operations.py
touch find_cutsites.py
#part 4
cd /workspaces/05-first-exam-mayakg01/bioinformatics_project/results
touch cutsite_summary.txt
#part 5
cd /workspaces/05-first-exam-mayakg01/bioinformatics_project/data
touch random_sequence.fasta
#part 6
cd /workspaces/05-first-exam-mayakg01/bioinformatics_project
touch README_new.md