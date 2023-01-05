#problem - https://rosalind.info/problems/dna/
#solution

def nucleotide_counter(dna):
    DNA = dna
    
    A_counter = 0
    T_counter = 0
    G_counter = 0
    C_counter = 0
    
    for i in DNA:
        if (i == "A"):
            A_counter += 1
        if (i == "T"):
            T_counter += 1
        if (i == "G"):
            G_counter += 1
        if (i == "C"):
            C_counter += 1
            
    return(A_counter, C_counter,  G_counter,T_counter )

print(nucleotide_counter("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))
