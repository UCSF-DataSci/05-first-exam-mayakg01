import sys
import re
add_amount = sys.argv[2].find("|")
add_amount
with open (sys.argv[1], 'r') as file:
    fasta_file = file.read().replace('\n', '')
indices = [i.start() + add_amount for i in re.finditer(sys.argv[2].replace("|", ''), fasta_file)]
key_counter = 1
cut_sites = {}
for i in range(len(indices)):
    for j in range(i+1, len(indices)):
        if indices[j] - indices[i] >= 80000 and indices[j] - indices[i] <= 120000:
            cut_sites[key_counter] = str(indices[i]) + ' - ' + str(indices[j])
            key_counter += 1
f = open("results/cutsite_summary.txt", "w")            
print("Analyzing cut site: " + sys.argv[2])
f.write("Analyzing cut site: " + sys.argv[2] + "\n")
##print(sys.argv[2])
print("Total cut sites found: " + str(len(indices)))
f.write("Total cut sites found: " + str(len(indices)) + "\n")
print("Cut site pairs 80-120 kbp apart: " + str(len(cut_sites)))
f.write("Cut site pairs 80-120 kbp apart: " + str(len(cut_sites)) + "\n")
print("First 5 pairs:")
f.write("First 5 pairs:" + "\n")
for i in range(1,6):
    print(str(i) + ". " + cut_sites[i])
    f.write(str(i) + ". " + cut_sites[i])
    f.write("\n")
f.close()    
    


