def max_num(num_1,num_2,num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_2 >=num_1 and num_2 >=num_3:
        return num_2
    else:
        return num_3

print(max_num(83,46,75))

arr = [3,4,56,64,4,346,36,86,65,86,5,66,57]
temp = 0
for index in range(len(arr)):
    # print(index)
    if index % 4 == 0 and arr[index] >= temp:
        temp = arr[index]
        # index+=2
        print(index)

print(temp)
print(index)


for index in range(1,len(arr),2):
    if  arr[index] >= temp:
        temp = arr[index]
        print(index)

print(temp)
print(index)
# x=45
# for x in arr:
#     if arr.index(x) % 4 == 0 and x >= temp:
#         temp = x
# print(temp)
# print(x)
#
# print(arr.index(x))

