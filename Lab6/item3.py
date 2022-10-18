def power(N, P):
    if P == 0:  
        return 1
   
    return (N*power(N, P-1)) 
 
N,P = input('Enter Input a b : ').split()
 
print(power(int(N), int(P)))