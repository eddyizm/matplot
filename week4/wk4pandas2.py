# week 4 pandas
# creation and manipulation
import pandas as pd
import string
#from string import lower
# Adding a Column 
'''
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
'''
# Add columns here
'''
df['Sold in Bulk?'] = ['Yes', 'Yes','No', 'No']
print(df)
'''
# Adding a Column || 
'''
df['Is taxed?'] = 'Yes'
print(df)
'''
# Adding a Column ||| 
'''
df['Revenue'] = df.Price - df['Cost to Manufacture']
print(df)
'''
# Performing Column Operations
df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
  columns=['Name', 'Email']
)

# Add columns here
df['Lowercase Name'] = df['Name'].str.lower()
print(df)
# Renaming Columns
# must rename all columns when using this method
df.columns = ['Full Name', 'Email Address', 'Name in lowerCase']
print(df)
# Renaming Columns II
df.rename(columns={'Full Name':'Tuple bitch!'}, inplace=True)
print(df)