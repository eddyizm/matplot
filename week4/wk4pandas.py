# week 4 - pandas
import pandas as pd
import xlrd
# # sample data 
# df = pd.read_excel(r'C:\Users\ecervantes\Downloads\Mourning Warbler Data.xlsx')
# #print(df.head(100))
# #df[(df.shoe_type == 'sandals') & (df.shoe_color == 'black')]
# filtered_none = df[df.Julian == 155.0]
# print (filtered_none)

# CREATING, LOADING, AND SELECTING DATA WITH PANDAS
# 2/15 - Create a DataFrame I
'''
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)
'''
# 3/15 Create a DataFrame II
'''
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=['Store ID','Location', 'Number of Employees'
    #add column names here
  ])

print(df2)
'''
# 4/15 Comma Separated Variables (CSV)
'''
name,cake_flavor,frosting_flavor,topping
Devil's Food,chocolate,chocolate,chocolate shavings
Birthday Cake,vanilla,vanilla,rainbow sprinkles
Carrot Cake,carrot,cream cheese,almonds
'''
# 5/15 Loading and Saving CSVs
'''
df = pd.read_csv('sample.csv')
print(df)
'''
# 6/15 Inspect a DataFrame
'''
df = pd.read_csv('imdb.csv')
print(df.head())
print(df.info())
# info returned
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 220 entries, 0 to 219
# Data columns (total 5 columns):
# id             220 non-null int64
# name           220 non-null object
# genre          220 non-null object
# year           220 non-null int64
# imdb_rating    220 non-null float64
# dtypes: float64(1), int64(2), object(2)
# memory usage: 8.7+ KB
# None
'''
# 7/15 Select Columns
clinic_data = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])
'''
df = clinic_data
clinic_north = df.clinic_north
print(type(clinic_north))
print (type(df))
print (clinic_north)
''' 
# 8/15 Selecting Multiple Columns
'''
df = clinic_data
clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))
'''
# 9/15 Select Rows 
'''
df = clinic_data
march = df.iloc[2]
#print (type(march))
print (march)
print (df.head())
'''
# 10/15 Selecting Multiple Rows
'''
df = clinic_data
april_may_june = df.iloc[3:6]
print (april_may_june)
'''
# 11/15 Select Rows with Logic I
'''


january = df[df.month == 'January']           
print (january)
'''
# 12/15 Select Rows with Logic II
'''
df = clinic_data
march_april = df[(df.month == 'March')| (df.month == 'April')]           
print (march_april)
'''
# 13/15 Select Rows with Logic III
'''
df = clinic_data
january_february_march = df[df.month.isin(['January', 'February', 'March'])]           
print(january_february_march)
'''
# 14/15 Setting indices
'''
df = clinic_data
df2 = df.loc[[1, 3, 5]]
#print(df2)
df3 = df2.reset_index(inplace=True, drop=True)
print(df3)
'''
# 15/15 Review
orders = pd.read_csv('week4\shoefly.csv')
#print (orders.head())
emails = orders.email
print(emails)
