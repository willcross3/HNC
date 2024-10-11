#print prime factors
 
import math
 
# A function to print all prime factors of
# a given number n
'''def primeFactors(n):
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n // 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            print(i),
            n = n // i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n),
        '''
         

def is_prime(num):
    #Check if a number is prime.
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Calculate 2^n - 1 for n in the range of 0 to 50
for n in range(51):
    result = 2**n - 1
    prime_status = "prime" if is_prime(result) else "not prime"
    print(f"2^{n} - 1 = {result} is {prime_status}")


# Driver Program to test above function
n = int(input("Enter the number you would like the prime factors for: "))
primeFactors(n)