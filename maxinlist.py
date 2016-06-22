# find max value in list
myl = [2, 10, 33, 45, 67, 89]
print reduce(lambda a,b : a if a > b else b , myl)
