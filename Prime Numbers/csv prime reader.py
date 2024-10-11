import csv

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def read_csv_and_find_primes(filename):
    """Read a CSV file and find prime numbers in it."""
    primes = []
    
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for num_str in row:
                try:
                    num = int(num_str)
                    if is_prime(num):
                        primes.append(num)
                except ValueError:
                    continue  # Ignore non-integer values
    
    return primes

# Example usage
filename = r"C:\Users\WILLCROSS\Desktop\Prime Numbers\allnumbers.csv"
prime_numbers = read_csv_and_find_primes(filename)
print("Prime numbers found:", prime_numbers)