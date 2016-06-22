# list of square of all odd numbers from 1 to 10
sqol = [x ** 2 for x in range(1,11) if x % 2 == 1]
print sqol

# power of 2 till 10
potl = [2 ** x for x in range(0,11)]
print potl

# list of prime number from 1 to 20
noprimes = [j for i in range(2, 8) for j in range(i*2, 20, i)]
print noprimes
primes = [x for x in range(2,20) if x not in noprimes]
print primes
