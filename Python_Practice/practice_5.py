# Exponent function with for loop 2**3
print(2**4)
def raise_to_power(base_num,pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(2,4))

#2D Lists-Nested Loops

number_grid =[
    [0,1,2,3,4],
    [4,5,6,8],
    [5,2,4],
    [0,3],
    [4]
]
print(number_grid[0])
print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)






