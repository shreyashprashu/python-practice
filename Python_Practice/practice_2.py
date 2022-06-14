# def cube(num):
#     return pow(num,5)
#
# print(cube(3))
is_male = False
is_tall = False
# print("press Y/N ")
# male = input("Are you Male?")
# tall = input("Are you Tall?")
#
# if male == "Y":
#     is_male = True
# elif male == "N":
#     is_male = False
# else:
#     print ("PLEASE ENTER A  VALID INPUT")
#
# if tall == "Y":
#     is_tall = True
# elif tall == "N":
#     is_tall =False
# else:
#     print("PLEASE ENTER A  VALID INPUT")

if is_male and is_tall:
    print("you are a male and tall")
elif is_male and not(is_tall):
    print(" you are a male but  not tall")
elif not(is_male) and is_tall:
    print("you are not male but tall")
else:
    print("you are not male and not tall")

