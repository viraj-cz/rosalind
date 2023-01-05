#problem - https://rosalind.info/problems/fib/

#solution

#this is a simple fibonacci sequence -- we use dynammic programming concepts to solve this

def no_of_rabbits(month, birth):
    N = month
    K = birth
    month_values = [1,1]
    for i in range(2,N):
        fibonacci_formula = month_values[i-1] + (K*month_values[i-2]) #I have modified the formula here for k pairs
        month_values.append(fibonacci_formula)
        
    return(month_values[len(month_values)-1])

    
print(no_of_rabbits(36,5))
