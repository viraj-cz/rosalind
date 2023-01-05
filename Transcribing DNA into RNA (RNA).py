
#problem - https://rosalind.info/problems/rna/
#solution

def dna_to_rna(dna):
    DNA = dna
    RNA = DNA.replace("T", "U")

    return(RNA)

print(dna_to_rna("GATGGAACTTGACTACGTAAATT"))
