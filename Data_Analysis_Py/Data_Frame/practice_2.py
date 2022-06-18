import pandas
import numpy as np

xls = pandas.ExcelFile("yelp.xlsx")
# df = xls.parse('yelp_data')
# print(df.shape)

print(xls.sheet_names)

# df= xls.parse("yelp_data",usecols=[1,2,3])
df= xls.parse("yelp_data")
# print(df[["name","take_out"]])

# df["review_count"] = pandas.to_numeric(df["review_count"],errors='coerce')
# print(df["review_count"])
# df["stars"] = df["stars"].astype(str)
# print(df["stars"].str.replace(".","_"))

# print(df.head())

df_cities = xls.parse("cities")
# print(df_cities.head())

df_states = xls.parse("states")
# print(df_states.head())

df = pandas.merge(left=df, right=df_cities, how="inner", left_on="city_id", right_on="id")
# print(df.head())

df = pandas.merge(left=df, right=df_states, how="inner", left_on="state_id", right_on="id")
# print(df.head(15))

# print(df.shape)
# print(df[388:456])

# atts=['name','city','state']
# print(df[atts].head())

del df['id_y']
del df['id_x']
print(df.head())
#
# last_index_df = len(df)- 1
# last_business = df[last_index_df:]
# print(last_business["name"])
#
# belle = df["city"] == "Bellevue"
# print(belle)
# print(df[belle])

# lv = df["city"] == "Las Vegas"
# cat_0_bars = df["category_0"]=="Dive Bars"
# cat_1_bars = df["category_1"]=="Dive Bars"
# dive_bars_lv = df[lv & (cat_0_bars | cat_1_bars)]
# print(len(dive_bars_lv))

# star = dive_bars_lv["stars"] >= 4.0
# print(dive_bars_lv[star])


# print(df.groupby(['city']).groups.keys())

# city_stars = df.groupby(['city']).agg([np.sum,np.mean,np.std])['stars']
# print(city_stars)

bars_rest = df['category_0'].isin(['Bars','Restaurants'])
df_bars_rest = df[bars_rest]
# print(df_bars_rest)
pivot_state_cat = pandas.pivot_table(df_bars_rest , index=['state','city','category_0'])
pivot_state_cat = [['review count', 'stars']]
print(pivot_state_cat)




