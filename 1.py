a = list(range(1,1000))
b = [x for x in a if x%3 == 0 or x%5 == 0 ]
print(sum(b))
