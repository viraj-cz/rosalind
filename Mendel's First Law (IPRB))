

#problem: https://rosalind.info/problems/iprb/

#solution:

def dominant_progeny(K,M,N):
    #Probablity of picking up that pair:
    no_of_K = K #homzygus dominant
    no_of_M = M #hetrozygus
    no_of_N = N #homozygus recissive
    no_of_all = no_of_K + no_of_M + no_of_N

    #Probablity of a dominant Allele in pair combinations
    #found using Punnet Squares
    KK = 1
    KM = 1
    KN = 1
    
    MK = 1
    MM = 0.75
    MN = 0.5
    
    NK = 1
    NM = 0.5
    NN = 0
    
    #probabilities of picking up each base pair:
    pick_KK = (no_of_K / no_of_all)*((no_of_K-1) / (no_of_all-1))
    pick_KM = (no_of_K / no_of_all)*(no_of_M / (no_of_all-1))
    pick_KN = (no_of_K / no_of_all)*(no_of_N / (no_of_all-1))
    
    pick_MK = (no_of_M / no_of_all)*(no_of_K / (no_of_all-1))
    pick_MM = (no_of_M / no_of_all)*((no_of_M -1) / (no_of_all-1))
    pick_MN = (no_of_M / no_of_all)*(no_of_N / (no_of_all-1))
    
    pick_NK = (no_of_N / no_of_all)*(no_of_K / (no_of_all-1))
    pick_NM = (no_of_N / no_of_all)*(no_of_M / (no_of_all-1))
    pick_NN = (no_of_N / no_of_all)*((no_of_N -1) / (no_of_all-1))
    
    #Final Probablity of picking up a dominant progeny:
    final_prob = (pick_KK * KK) + (pick_KM * KM) + (pick_KN * KN) + (pick_MK * MK) + (pick_MM * MM) + (pick_MN * MN) + (pick_NK * NK) + (pick_NM * NM) + (pick_NN * NN)

    return(final_prob)
    
print(dominant_progeny(2,2,2))
