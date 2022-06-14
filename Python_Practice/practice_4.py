monthConversions ={
    "Jan": "January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "June": "June"
}

print(monthConversions["Mar"])
print(monthConversions.get("Jan", "Not a valid Key"))
# key = input("Enter a key:").casefold()
# if key == monthConversions.get(key.title(),"Not a valid key").casefold():
#     print(monthConversions(key.title()))

for i in monthConversions:
    print(i,monthConversions[i])

