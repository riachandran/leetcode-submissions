import math
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        is_prime = [False,False] + [True]*(n-1) 
        #Sieve of Eratosthenes
        for i in range(2,int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i,n+1,i):
                    is_prime[j] = False

        
        prime_count = sum(is_prime[1:n+1])
        non_prime_count = n - prime_count

        return (math.factorial(prime_count)*math.factorial(non_prime_count)) % (10**9+7)
