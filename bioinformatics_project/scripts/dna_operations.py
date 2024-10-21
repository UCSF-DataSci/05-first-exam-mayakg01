import sys
def complement(sequence):
    complement_definitions = dict(a = 'T', A= 'T', t='A', T='A', c='G', C='G', g='C', G='C')
    comp = []
    for i in sequence:
        comp.append(complement_definitions[i])
    return ''.join(comp)

def reverse(sequence):
    seq = list(sequence)
    rev = []
    while len(seq) > 0:
        rev.append(seq.pop().upper())
    return ''.join(rev)

def reverse_complement(sequence):
    rev = reverse(sequence)
    return complement(rev)

print("Original Sequence:" + sys.argv[1])
print("Complement: " + complement(sys.argv[1]))
print("Reverse:" + reverse(sys.argv[1]))
print("Reverse Complement:" + reverse_complement(sys.argv[1]))


