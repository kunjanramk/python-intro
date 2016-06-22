# filtering odd numbers from range 1 to 50
lodd = filter(lambda x : x % 2 == 1, range(1,50))
print lodd

# filtering odd square which are divisible by 5
losqdf = filter(lambda x : x % 5 == 0, [x ** 2 for x in range(1,50) if x % 2 == 1])
print losqdf
