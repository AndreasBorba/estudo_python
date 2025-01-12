dimensions = (200, 60)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

print('\nOriginal dimension:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimension:')
for dimension in dimensions:
    print(dimension)