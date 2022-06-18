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
# print(df.head())

df_pitts = df[df['city'] == 'Pittsburgh']
# print(df_pitts.head())
df_vegas = df[df['city'] == 'Las Vegas']
# print(df_vegas.head())

pitts_stars = df_pitts['stars']
vegas_stars = df_vegas['stars']
print(pitts_stars.head())
print(vegas_stars.head())

# plt.hist(
#     pitts_stars,
#     alpha = 0.3,
#     color='yellow',
#     label='Pittsburgh',
#     bins='auto'
# )
# plt.hist(
#     vegas_stars,
#     alpha = 0.3,
#     color='red',
#     label='Las Vegas',
#     bins='auto'
# )
#
#
# plt.xlabel('Rating')
# plt.ylabel('Number of Rating scores')
# plt.legend(loc='best')
# plt.title('Review distribution of Pittsburgh and Las Vegas')
# plt.show()

plt.hist(
    [pitts_stars,vegas_stars],
    alpha=0.7,
    color=['red','blue'],
    label=['Pittsburgh','Las Vegas'],
    bins='auto'
)
plt.xlabel('Rating')
plt.ylabel('Number of Rating scores')
plt.legend(loc='best')
plt.title('Review distribution of Pittsburgh and Las Vegas')
plt.show()




