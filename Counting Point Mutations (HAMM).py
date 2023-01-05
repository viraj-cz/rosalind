#problem - https://rosalind.info/problems/hamm/

#solution

def hamming_distance(wild_type, mutation):
    
    diff_nucleotides = 0
    bigger_strand = max(wild_type, mutation)
    
    for i in range(len(bigger_strand)):
        if(wild_type[i] != mutation[i]):
            diff_nucleotides += 1

    return(diff_nucleotides)

print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
