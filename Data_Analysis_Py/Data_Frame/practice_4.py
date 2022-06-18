import matplotlib.pyplot as plt
import pandas

xls = pandas.ExcelFile("yelp.xlsx")
df = xls.parse("yelp_data")

df_cities = xls.parse("cities")
df_states = xls.parse("states")

df = pandas.merge(left=df, right=df_cities, how="inner", left_on="city_id", right_on="id")
df = pandas.merge(left=df, right=df_states, how="inner", left_on="state_id", right_on="id")
del df['id_y']
del df['id_x']

df_health = df[df["category_0"] == "Health & Medical"]
df_fast =df[df["category_0"] == "Fast Food"]
df_break = df[df["category_0"]== "Breakfast & Brunch"]

plt.scatter(
    df_health["stars"],df_health["review_count"],
    marker='o',
    color='r',
    # aplha= 0.7,
    s =124,
    label=["Health & Medical"]
)
plt.scatter(
    df_fast["stars"],df_fast["review_count"],
    marker='h',
    color='g',
    # aplha= 0.7,
    s =124,
    label=["Fast Food"]
)
plt.scatter(
    df_break["stars"],df_break["review_count"],
    marker='^',
    color='b',
    # aplha= 0.7,
    s =124,
    label=["Breakfast & Brunch"]
)
plt.xlabel('Rating')
plt.ylabel('Review Count')
plt.legend(loc='upper left')
axes = plt.gca()
axes.set_yscale('log')
plt.show()

