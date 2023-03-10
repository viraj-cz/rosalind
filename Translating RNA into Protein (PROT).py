
# Online Python - IDE, Editor, Compiler, Interpreter


def rna_to_protein(rna):
    RNA = rna
    
    for i in range(len(RNA)-2):
        protein_string = ""
        ORF = []
        stop_codons = []
        
        #detecting the start codon
        if ((RNA[i] == "A") and (RNA[i+1] == "U") and (RNA[i+2] == "G")):
            start_codon = i
            break
            protein_string += "M"
            
    #building the ORF
    start_pos = len(RNA) - start_codon
    for i in range(int(start_pos/3)): #int() converts it to a integer and takes all the decimals away
        try:
            p1 = (start_codon) + (3 * i)
            p2 = (p1+3)
            ORF.append(RNA[p1:p2])
        except:
            pass
            #what we are basically doing is putting the ORF in array
            #but there is a possibility that, it might fail because of an ORF like [AUG GCC TA]
            #cause TA is not 3 elements long
            #so we just pass it when it fails, cause be don't need the last two elements anyways
        
    #finding the stop codon
    stop_codon = None
    for i in range(len(ORF)):
        if(ORF[i] == "UAA" or ORF[i] == "UAG" or ORF[i] == "UGA"):
            stop_codon = i
            break
        #we break cause we only want to find the first stop codon in ORF
            
    
    #now finally converting to protein_strings
    for i in range(len(ORF)):
        if (ORF[i] == "UAA" or ORF[i] == "UAG" or ORF[i] == "UGA" ):
            break
        if(ORF[i] == "GCU" or ORF[i] == "GCC" or ORF[i] == "GCA" or ORF[i] == "GCG"):
            protein_string += "A"
        if(ORF[i] == "UGU" or ORF[i] == "UGC"):
            protein_string += "C"
        if(ORF[i] == "GAU" or ORF[i] == "GAC"):
            protein_string += "D"
        if(ORF[i] == "GAA" or ORF[i] == "GAG"):
            protein_string += "E"
        if(ORF[i] == "UUU" or ORF[i] == "UUC"):
            protein_string += "F"
        if(ORF[i] == "GGU" or ORF[i] == "GGC" or ORF[i] == "GGA" or ORF[i] == "GGG"):
            protein_string += "G"
        if(ORF[i] == "CAU" or ORF[i] == "CAC"):
            protein_string += "H"
        if(ORF[i] == "AUU" or ORF[i] == "AUC" or ORF[i] == "AUA"):
            protein_string += "I"
        if(ORF[i] == "AAA" or ORF[i] == "AAG"):
            protein_string += "K"
        if(ORF[i] == "UUA" or ORF[i] == "UUG" or ORF[i] == "CUU" or ORF[i] == "CUC" or ORF[i] == "CUA" or ORF[i] == "CUG"):
            protein_string += "L"
        if(ORF[i] == "AUG"):
            protein_string += "M"
        if(ORF[i] == "AAU" or ORF[i] == "AAC"):
            protein_string += "N"
        if(ORF[i] == "CCU" or ORF[i] == "CCC" or ORF[i] == "CCA" or ORF[i] == "CCG"):
            protein_string += "P"   
        if(ORF[i] == "CAA" or ORF[i] == "CAG"):
            protein_string += "Q"  
        if(ORF[i] == "CGU" or ORF[i] == "CGC" or ORF[i] == "CGA" or ORF[i] == "CGG" or ORF[i] == "AGA" or ORF[i] == "AGG"):
            protein_string += "R" 
        if(ORF[i] == "UCU" or ORF[i] == "UCC" or ORF[i] == "UCA" or ORF[i] == "UCG" or ORF[i] == "AGU" or ORF[i] == "AGC"):
            protein_string += "S"    
        if(ORF[i] == "ACU" or ORF[i] == "ACC" or ORF[i] == "ACA" or ORF[i] == "ACG"):
            protein_string += "T"
        if(ORF[i] == "GUU" or ORF[i] == "GUC" or ORF[i] == "GUA" or ORF[i] == "GUG"):
            protein_string += "V"   
        if(ORF[i] == "UGG"):
            protein_string += "W"    
        if(ORF[i] == "UAU" or ORF[i] == "UAC"):
            protein_string += "Y" 
    return(protein_string)
        
        
print(rna_to_protein("AUGGCCUGCGUGCUCGGUAGCGUUAGAGGGCAUUAUAGGCGCUUGCGAUAUGAUGACCGCAGAGCUGGGUCGUCGGCUUGUUAUCUCAGACGACCUCCCUUAGCUCCCCACACGUGUCCUUGUCAAAUCUCUACCGUCUCUCGUCCGACAGAAUUUAAAAGCUUAGGGGUGUCGGCCAUCAGGUCCCGUUACAUGGAUUCAUUACUGAGCAAUCGGUUCUCUCUUCCACACUCAGUGUCUACUGGAAUUGGGCUGCCGAAGUUCUUGGCCCGACUGCAACACGAUUGUGGGCCCUGCCAUCAUCGAGGAGCUCUGCUCCUGCCUACUAUUGCCACUCUGAAGGGGUUGAUCCUUCCGUUAGGAUGGAGUGCUUCUUCGCUCCGCUAUACCAAAGGGGAACAGCAAAAAGCGGUUCAAAUUGGGGAAGCUUACGGCGCCGGGUUCAAUCUCUGUAAAGCAGGCCGACAGGCGUUUGCAUGUCUGUACCCUCAUAAUCACCUAGUUCCAGCCGAGUUCGGCCUAACUACGCAUUACAUACGUCCACGCUGGACUCAACAAGACCACGGUAUCCCUUCAGGCAGCGAACCUAUUGCUAGCUGUGAUGAUACGGCGGCACACCACGCGUCCACGGCUGAGCCGGUGGUUCAGUGCGCGGAGCCCCGUCUGCUGUUCGACCGGCCAACUCUCGUGAUGAAGGCUACCGCAAAGGCCCUUUCAAGAAUCAUGAAACACAUCAGCCGGGCGCAUGGACCGUAUGUGAUCAAUAGGAGCUGCACUCGUACAGUAAGUACUUUUGCCCAACUGCAGGUCCUAUGUGGGUUAUAUGAGACCAACCGGACUCUAGAGGGUUCUUUCAGCCUGAACAGGGUAUUGGUGAACGGUAGAAGGAAACUCUUACCAAGCCAUAAAAGAAAGGGUAGAGGAGUGGUACGGUGUCAGCCCCGGCAGCUUGACAAUCCCAUGUCAAAUUCCACACAACCAUGUCCAAUUAGUCGUCCAACCAUAUUUUGGCAUUGGACAUCCAUCCUUAAUCCCGGACUGCGGACACAGAACAUAGGCCCGCCCCCGUUCCAGUUCCGACUUUUAGGCCAUAAAUCACACAUUGAUAAUCAACGCUUCCUGCGGCUACGAAGCGUGGCCCGUGGCCAUCCUCGUACACCCUUAAUAGUAGUGCCGAUACAGAUGCAAGCCCCCGUGAUAAAUAGUACCAGCGCAGGGGGUAAAAGCUAUUUCUGGCCGACAUCGCUUAUUAUGUCCGGUUUCUAUUUUGUGCUUGCUGCGCGGCCAGUAACGUACAUGACAUAUAGAAGUAGACUGUGUUCUCGGCGCCUAGAAAUUGCCAUCAGCCUCAAACUAACACGGUAUCACGACGUUGGCCCGUGUGUCACUAUUGUUAAAGGCCUUUGCUGCCAUAGGGGAGCUCUUGUAAGCUGCGUCUCGUCGGCCAAUUCGGAUUUGUGGCCCUGCCCGGUUGAAUUAACGAUCAAGAUCCCAAAGAAACCAGCAGGGGACUCCCAUGCGAAACUGCGACGUGGAAGAGGGCCGGCCGCGUUCCUUAGACCCGAUCCGUCUUUAGGAGAGGCACUAUUUGGGGGCUCAAUUCUACGAGCCCCCUGCAUCCAAAAGACAGCCCGUCCCCCCGGACAGCUGAUACAUUGUGAGCCUUUCAAGGUAUGGCUUCGUGGCCCUCUCUUUAGCCAAGGGUUGUUCCAGUGCGACGGGUCAGAUCCUGUACCCCUUUCUGGGAUCCACUGGGAUGGACCGCGAUUAUCACUCCCAAGUGGUACGAGAGGCAGUUCGGAUGGUUUCAUGGUUGGCAACAGCGCCUCUCCAACGAACUCAGCAUGGUACCGUUCGGGAAACGUGGCGACUACCCCCCCAUGGCAUUCGAAUUACGGUCGCCCUUGUCCGCCUAUUUCUUCUACCACGAAACAAACUAAUUCAACUCGAGAGGCGAGCACAAUUCCUGAACCUUGCAAGGAAGGAUUGCAUCUGUAUAUUUCGGGAAAAUCGAGCGGAGGGUCCUCAUACAACAGCAGUCCCUCGAUACAAGAAGAGGUGCUGUUGCUACCGGCCUAUACCUAUCAACAGUUGUCCUCACAUAGGAUUGCAGUUUCUACUAACUUGCGCUACCCGCACUACGGUGUCAUGACUGCAGUGGAACGCGCCCAUCAUUUUCUGUUGCUAUUCGACGGGUCACAUUUGAGGUGCAAGAUUUACGCGGGAGGUUGUCGCAAAUAUGGUUCCGCGCGACGCGCCAGAUUGACUGCAGAGGGUUACGGUCACCGUUUUAUCUCACGACACCAACUAUGCGCCUCGUUAAGUAAGAUACCAAGGUUAGGAUCGGAAAAUAAUAUCUAUGAGGAACCCUCUCGUCCCUUCAACUGGAUGACCAUAUACCCCGUCAAACUGCUCGAGGAAAACAAAUGGUCUACAUCUGUAUGGUUUACGAUUUUAAGAAAACAUCGCGCCCCUGUCUGUUCUAGACGCCCGCCUAGUUCGAUAGUGCCCCGUCGCGGUCGUCUAAGAAGGGGCCUCAAUCUGUCGUGGGCGUUUUGUGAUCGGCCACUGGGUGGAUACCCAAUGCGCAAGAACACCAAUCGAAGGCGUGCGCUUGAAUUCAGUGUCGAAGGCAAAGAUAACAGGUUCGCAUAUGUGGAUCCAUUGAUAUGGAGGGUUUGUGGAACAGCGCCACGUAAUUGGCAUGUUAUGCGUGGGUAUCUGGACCGGCCAUCUAUGGCGACCGGAAUCCAUGCCCUGAUUAGCAGGUACGGAUUGAACGUAUACAAUGUCGUGUGUAACUGGGCCGCCACUGGAUAUGAGGUAUGCAACGGGCCAGUUUCUCCGUUCCCAACCCUGAGUCGCGGAUAUAUAGGAUGUCAUGCACCUAGUGCAAUAAUCCAGGACUCAUUCAUAUGGCUAAGAAGUGUGCGGCGGAGACAGGGGACCAUCGAUCUCUUUAGACGUACGGUAAUGAUAAAAGACAGCUCUGCAUUAAGGGCAUACGGAGACACAGAGGGUAGUGGGUCAGUGAAUAGUAAAUGGUCUGCUGUAAUCGUCCGUAACGCGGCUGUUGUCAGAAUGCGGAACACGGAACAUCGCCGGGGGUUAACGCCCUCACGAACCAGUCUAUGGAACACAUGGGAUCGGACACUCAAAUAUCAGGCGAGGUAUCAUUUGGUGUGCGUUGCGGCGGCCGCACGGACGACAACCGUUGUAAGCCUAGGCAUCAGUGAGUUUAGGACGAAGCUUUUCGUGCGGAGACGUUUGAUGGUGAGCAAGCGCAUGCAAACCCAUACGCAUGGCACGUGCCAUCUGAGAGGUCUUGACCCGAUUACAUUGGGUGCGACAUGGCGACGGCUUAUCAUUGGCAUGCUAGGCGUCUGUUGUGUUAGAUGUCUCCCAUUUUGGUCGUUAGCGAGGAGUGGUAGUUGGCCUGAAUGUGGAUACUCAGGUCUCAUUUUCAUAACAAUUUCAUAUAGGAUUCCAUCCCGUACCAGCUACACAGACCGUGUAAGCAGUCCGACUUUCCCCUAUAUGGCGUUUUAUUGGACAUGCCUGUAUGUAGGAUAUAGCGGCACUUCAGUGUUCCCCUCCACACUUGUCAGGGGCUUAUCCUGCCUUGCUUCGCACAGUGUUGAUUGCCAGUACGUGAAGCCAAAAAUUGAGCGGACUCUCGUUGAAUGUCAGCCAUACCACCAUAAGAAGUUGCCCGCACGCGAAAACAUGCAACUCCAGAUUUCUGGGUCCCAUAGUCAGAGCUCUUGCGGCGCGAACGAACCUACAGUGAUUAGCGUGUUGAAUAUUUCCAGAACCGUUGCAUAUCUGUACACGAGUGACAUUUUUGAUCGGGGCAUCGUUACAAUGCCCGGAACGUUGCCCAAUCCUAUUGCUCUCCUUCCAUUGAUUAGGAUCUCGAUCAACGCCACGGUCAGGAAACCACUCUACUACGCACGCCGCCUAGGGGCAGCGGCUCGAUUAAUCCCCUAUGCUAGCUAUCCUUAUGCUAUGAUACGGCGGAAAAUAGUGCCGUUCUCAAACAUCUGCAGCAAUGGUGGGAUGAGGACGCAAUCGAAUUCGCUUCGUCUGCCUACGUGGAUGCGCAGCAGCCGCGUCGCAGAAAUCCUCGGUCGCAGUUCUGGAACCCGGUUGGGCCCGGAGGGUGCUCCCCGGGCGACCGAAGCUACCAUGUACCACAAUAUGGUGGACCCUGUAGCACCGAGCCAUCCUUCAAAGACGGUUUGGAAAGCGCCGUUCGAUGGGACCGCGCCUCAUACUAAAUCUCACACCAGUGGGAGAUCUAACCCAUCAUCAAUAUUAGGUACGGUGGAACGUAAUUCGAGUCCGAGGGGAGGAACAGAAAGAGUAGUAACCGAGCCGCUAUGCAGCUGUUGUUCACGGGUCGAUGGCUCUUAUUUCUUGAUUUAUAUUGACGCCACCCUCACACCUGGCCGCCUUUCACUCUGCAUUAGGGAAAUCAGGUCAGUGAGCCAUGCUUUAAGGGAAAUCCCUCAUGAGGGUCGUCAUCAGUUCCCACUGGUAUGCAAGCAGCAUGCCGGAAGUAAACUUCUAUUUAGAGGCAACUGCAUAAACUCCCAUCCUGCGCGUAUAACUGGGUGGGCGGGCAGACGGUUGCAGCGGCAACAUAUACGUCUACUGUCAGUUGAUAUCGCAUCGGGUGAACAGGGACAGCAGCAAUGCACCAUAUGGUUCGGGAGUAGUGUGCUUGCUACUGUAGUGGCCAGUUCCUCGUGUACACACUGUAUCGUGGCGGUUGUUCGUAAUGUGUGUAGUUCUAACAACGGACACCCCUAUCUCACCGCUAGCCCCUAUAUUGACCGAAUCGCAAUCGUUGUCGAAGCACGUGCCACGCUCCGGUUCCUUCUCCCCUACCGUACACGACUUCCCACCCAAGUCCCAAAGAUCGCAUACGUGGCACCAUCCCAACCCAGGCCGCAAUCCCUCUCUCCUUCAUCCCACGGUCUGCGCUUGUCUUCGAGUGUCGCCUUAUCCGCAAGACGUAGUAUCAGGUGCGUCAACGGGCGCCAAAGAUUCUUGGGUUUCCCCUUAGUAUUGCUCAGCGCUCAAUCCUGGGGCAGAACCAUGUCAACUAGUCGCUCGCCGGCUGGAGCUUAUCUGCCGGCACGAGCGGAUUAUGACAUCACUGCAAUAGUAUAUGCAAAUACCUGGCCCUACGUACAUAGCGGGGGUACUCAGUUCGAGCGCCUAACUGGCUUAUACGAUCUUUGUCGAUCUGCUAGUGUAUGUGCACACACUUUAACGGUGUAUCGGUGCCCCAAUAGCUCGCCUGACAGCAAUGCCGGCACGGUUAAAAUAGAUUGUAUUUGUCUGUACAUACCAUUGGCCCCUCGGGGUUUCAAUGGACGAUUAAGAGAUUCUCGCUCGUACCGCCAGGGUCGGAAGGGGGUACUGAUGUACCCCCAUCUUACAGUGGACUGGUCCGUUAAUAAGUCCAUUCUCAGAGACUGUUUGAGACAUAGGGCGGUGCAUGUAACGGCAUCGCCGCCAGAACUGGACCAACUCCCCUACUCCCUUCGAAUGGGCGCAUUUAUAGAGCUAUGGGGCCCAGAUGACACUGUGUCGAAGAAUACUACGCGCUACGUGCAAUCAUUCCUUUGCGGUGCAAGAAUCGUCGCUGCAACAUAUCGAAACAUGGCUUUUGAACCGCAAGGUAACCACCGAACUAGGAUAAUGUCGCGCGAAACAGCCGUAUCUGGCGCCGUGCUUGUCACAGGUUUUAGUAUAUCCCGUUGUCCUGCGGCAAGGGCUUCUUGUGGGGAAGGGGGACCAUGCGCCUAUAAUUGUCAACCACCGGUCGCCAGCAGUCAUCACGAACGUACGGCAGUCUCUUCGACGUUUCCCGUCUGGCUGACAGCUAUCUUGUGCACAGUACACAUAAUUAGCGUAACAGUGAUAGGAGGGAUCACUGUCCCCAUCUUGUCAGGUCGAGUUCUGGCUCUACCAGAUAGACGUCCAUUCAAAUUCCACAGAGGCAUACCGCAACGCACGCAGGCUCAUCGAAGGAGAAAAACGAGUCAGUCAUAUUUCGUGACCCUGAUCUAUUGUGUACUGCAUUCCGAUGCAAUUAGCGCAUCCUCUGAGCUUAUAGAGAAUGCGAAUCUUGACCGGGAUGCAACAGGAUUUAAGCGGGCGGGUUUGAAUACCCUGAGCGCAAUGCAGGCCGGCACUUACUAUGUCAACCACACAAAGUUGAUCGGUGCCGAUAUAUUAACGUUGGCUAACCUUGACAAUAAGACCCCAAUGGGUAUUACUAUAUGUCUUUCCGUAUUAUCUAAGGAUCCUUAUAAGAUUUGUUACUUUGACAUACGAUAUAUCAUGACUCAAGUCAAUGGCGUGCACGGGUUGCGGAUAGAAGAGCCCCCGUACCCUCCAUCAACCAUGGUCCCUUGGAAUAUUAUAAUCAUACGAAGGUCGCUUAAGGAGCAUUUUGCUAGCUUUCUGGUAGCUCCUUUAAAUGAGAGACAGUUCUCUCCGUACCUACCACAUUACGCGGUCCUGAGCUGGGCAGCCUCGUGCAUAAAACUUAUCUAUCGCGGCCCCCGCGGAGCUUUAGUAGUUAUCGAUACCGCUUCUUUAUAUGAGAGGUUACACCUAUGCCUGCACUCCAAAGUCGAGUUAUCUGAUCCUUACGCGUCACAUGCGAACUCGCGACAGAUGGGAGGACUCUGCUGUCCGGCCCGCGAAAGAUUCGGCCAGACCAAACGUACAGACAUAGAGUCUCGACAGAUUCAGCUAACACGUGACUCUCCUGCAUUUUUCCCCUCGCAUAAAUUGGCAUGUGAAAGAGGACUGUUUACAUGGGUUCCUCCUUUGCGUCGCACCAAGGUGCAUCGCCGAACUAUCCACUUGGGGUUGCCUACUAAGGAGUAUGUCGUAGUUUGCACCCCGCACCCUAUCGGAAUCGUGUUGUUACAAUGCUUACUCGACUCAACAAACUGGACGCGACGAUGUUGCUAUUACGUCACUAGACUUAACGUCUCGACCAUCGAUAACGGGUUGGGAACAAGACCUAAUUUACUUGCCGCCUUUGAUUUCAUAGAUGCACUGGCCCACGCGCAACAACUUCCAGAUGAAGUAGCCAGCUCAUACAGUAUGCCCUUUAUGCAAAAACUCGCAUACGUACUGGCAUCUCUACAGAAAAGAAAAGCGGGGCGGAUACGCCUGCCAAGCUGCUUGAGCUGCCUCUUUCGGGGGCACCGGGGUCUCACGCAUCCCGAGCAUAUUGAAUGGGCCACACGACUUCAUCAUCUUGGAUCUGCUUCGUCCUGGUCAUUUCAACGCGAAUUCAUCAGUAAUAGAAACUACGCGUUCCAGACCGGGCUACCCAGGCCCGCUGUAGUUUACGUGAGCACACCGGUAGAUUUUGUUUUGCACAGACCUGAUUUUGCAACCAACGGAGCGAGGGGAAGGGGAAACUCAUACGCAACGCUCAGAGCAAUCUUCGAUUUUGUACGGCGUAGAAGCCAGGACGAUUUGCCACGGCGUUCCAGCUGUAUAGCAAAUAAGUGGUUGUUAAGAGUCCGCUGUCACAUCCCUGAGGUUCAUUGCAACUUAAAACUAACGCGGCGGAUUAGGCUUUUCGCAAACCGUCCCAAACGCGGUAGAAGCAGAUCUUCAGAAAGGUUGGGACUUGAUGGAAUCCUUAGUCUAUUAUCAACUGUGACUGGCGGGACUCUAGCAUCGGAGUUAUGCUGGUUAGUAAAUACAAAUGAAAGCUGGAUCAUGUGUAGGGUGAACCCUGAUUGCUAUUCCUUACGUUUCACGGAAGUGCUAAAACUCAAGUACCCUAGGCAUCGAUACAGAGCAGAAUUGGGCCGUGGCGUCAGAUAUAAAACGUAUCUUUUUUCCGCUCUGAGAGAACACACUGCCGUUGGCGUUCUUAAGUUGCAUCUCACCGGACAUCAGCCGUUACACGAUGGCCAAGCGACAUGUGGACCCAUAGACGGCGGGUGGACGAUGUAUGAAAGACCGCGAAGUCUUACCAUAUGGACACAGAAAUCAGCGUAUCCCCCCUUCAUAGAACGGCAUUAUCACAUAGAUAGCGGAGCGAAGUCCCUAAAACAUGUAGGACUGCAGUUACACAUCGGGGACUAUAAACCGUUGAGGCAAGGAAGAUUCGAGGAGUCUUUUGGCAUAUGUGGAUACGCCAAGUCCUGCUAUCAAGCAACUCUUGCGAGCCUGUUUAGUCACAACGUCCACUACCCAACCGCCACCAUCACGCCGGCCAGACUUAAUCUUCCGGUGGAAGUUCGGAUGUUGUCUCCUAAAGUAUUUUCUAUCGAGAGUGGUGGCCAUGGGUUCAAGGGGCGGUCAGGCUACGUAACCAGGCUAUGGAGUCGCAUUUUUUCCUUUGUCCUGCGCGACGGCGCUCGCCUACAUGUAGGCUCUACUGACAAGAUACACUCAACUGCGCGGGUUGACAUACUCGUAGACGCACUGCUUUCCCCCUCGGAGAUCAUGUCUCUAAGGUCGGCGCAUACCAUAAUUAUGUUUUUGUUUCCAACGACGGUGCUUCAUACAACAGAUAACGAGAUGGCCAUGGUGAGGGUACGACCGCCUUCACCAAUUAUCCCAGCAACCUCGAAGUUGCCCGUCUUUAUGUUCCCAGAAGUGCCCUACUUACAUUGGGUACUUUCUCUAGGACGGGAAUUUAGAGUGUGCCGAUACAUAAUAUACGUCACCAGUACACCAAUCACCCACUAUUAUAAAACCGUCAACCUUAUGCUAGGAUCUAAUUAUGUAUCGCCCAGCCAAGUUGUGCGCGCCCACGUAGGCUCUGGAUUAUGGACCUGGUUAAGACGGCCGCGAUCGCAGGCGCGUGCGAAGUCGAAAGAAUUGAGGCUCUUCGUAGGAGUCUUCCGCUGCUGGGUGUCAAAAUUGCUGCGCGUGGCACCAGUACCCAGCGCUGUCACUAGGAAUGUCAAGACUGAUUACCACACGUGGAAUCGCACGGAAAGCCUUGGACGUAACGCACCCCGAAUAAGCCCAACCGGAUGUGAAACAGAGCACUCUAACCCUAAGGGCCCGCGGCGCUCACAGUGUGAUCUGAGGCUGAUCAAGCUCUUCAACCGCUUGCCCCGAAGCAUUGUAUGUCACCUACAUUAUGUGAAGAAAGGGCGCCUAAGUAAGUCCUCAAGGCCACGAAGAAACCCUGGUUUGCCGAGGAAGCUGGGCGCGCCUCAAACGAAAGGAAAGCGAUUCUCUCGGUAUACAGUUAAAGAUCGGGCUCACCAUGUUGUGGGUGGAGUACGGUGCGCAAGCCGCCCAUGUGCUUCUAGCUUGACUUUCCACCGCGUCAGGGUGAGUUUUAUUCCCUACAUGUAUAAUUCAUACACUUCGUUAAGCUGGGUGGAAACCUGUAUGUUACACAAGAAGAAAUGUUACUCCGAGGUUGCACUAUGUAGGGGCCAUGGCAACAGGUCGAGUGGCUAUCGAUCUCUCGUUAUGGCCACAGCUUCAGUCAAGGAAAAACAGCUAUAUCCCGCACAUCGGUCUUCCGACUACACCACCAAAGGCUUGAUUACCGGUGAUCCGCCGAUCGGGAUGUGUCGAUAUUGCGUAACGCAUAGCUGUUCUGACAAUUCAACGAGGGAUCAUUGCUGCUCUUUCCCCACUGGCGGCUCAGCCAGGUUGAAGCGGCACCGAGCAACCCGGUGGUUCCAGCGGUCCUCAGACCUUGACCAUUGCAUCGUGUCAGGGCAUGUCGAUCGACAGGCGUGA"))
        
        
        

        
        
        
        
        
        
        

        
    
    
