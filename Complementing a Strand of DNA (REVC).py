#problem - https://rosalind.info/problems/revc/

#solution


def compliment_dna_strand(dna):
    DNA = dna
    CDNA = ""
    
    for i in range(len(DNA)):
        if(DNA[i] == "A"):
            CDNA += "T"
        if(DNA[i] == "T"):
            CDNA += "A"
        if(DNA[i] == "C"):
            CDNA += "G"
        if(DNA[i] == "G"):
            CDNA += "C"

    return(CDNA[::-1])

print(compliment_dna_strand("AAAACCCGGT"))
