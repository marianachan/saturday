#          0   1    2    3   4   5    6   7      8
#          -9  -8   -7   -6  -5  -4   -3  -2     -1
numbers = [6,  343, 57,  5,  4,  21,  3,  34545, 67]

x = numbers[8]
x = numbers[-1]
print(type(x), x)

y = numbers[3:6]
print(type(y), y)

z = numbers[7:8]
print(type(z), z)

j = numbers[0:4]
j = numbers[:4]
print(type(j), j)


f = numbers[6:9]
f = numbers[6:]
f = numbers[-3:]
print(f)
