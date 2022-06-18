import csv
# import os

# with open('albumlist.csv', 'r') as my_file:
#     reader = csv.DictReader(my_file)
#     print(type(reader))
#     count = 10
#
#     for row in reader:
#         # use break statement for escaping further iteration
#         # pass- anywhere continue-loops
#         count -= 1
#         if count >= 0:
#             print(row)
#         else:
#             break
#     print(count)
#
#     my_file.seek(0)
#
#     for row in reader:
#         count += 1
#         if count <= 9:
#             print(row)
#         else:
#             break
#     print(count)

with open("albumlist.csv", 'r') as my_file:
    reader = csv.DictReader(my_file)
    albums = []
    for row in reader:
        albums.append(row)

    # print(albums)
    print(len(albums))

# album_genre = [ row for row in albums if row["Genre"] == "Rock"][:10]
# print(album_genre)
#
# for row in album_genre:
#     print(row["Album"] , "by" ,row["Artist"])
#
# rock_albums = [ row for row in albums if (row["Genre"] == "Rock"
#                                      and ("Pop Rock" in row["Subgenre"] or "Fusion" in row["Subgenre"]))]
#
# print(len(rock_albums))
# for row in rock_albums:
#     print(row["Album"],"of genre",row["Genre"],"by",row["Artist"])

# release_years = [int(row["Year"]) for row in albums if row["Year"]]
# print(release_years)

def is_valid_year(string):
    try:
        year = int(string)
    except ValueError:
        return False    # or simply pass
    else:
        return year > 1800


release_years = [row["Year"] for row in albums if (is_valid_year(row["Year"]))]
print(release_years)
print(len(release_years))
min_release_date = min(release_years)
print(min_release_date)

valid_albums = [row for row in albums if (is_valid_year(row["Year"]))]
album_max = max(valid_albums, key=lambda x : x["Year"])
print(album_max["Artist"],album_max["Album"],album_max["Year"])
# print(len(valid_albums))
