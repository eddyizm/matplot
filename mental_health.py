# weekly data visualization project. 
# using dataset from kaggle.com 
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('env/OSMI Mental Health in Tech Survey 2017.csv')
#print(df.head(1))
# print(df.info())
# col = df.columns
# for c in col:
#   print(c)
df.rename(columns = 
{'Do you currently have a mental health disorder?':'Currently_Diagnosed', 
'Have you ever been diagnosed with a mental health disorder?':'Previously_Diagnosed',
'What is your age?':'Age', 'What is your gender?':'Gender'}, inplace = True)

age_sex = df[['Age', 'Gender', 
'Currently_Diagnosed',
'Previously_Diagnosed']]  
# df.rename(columns = {'$b':'B'}, inplace = True)

print(age_sex.head())
print(age_sex.info())

#march_april = df[(df.month == 'March')| (df.month == 'April')]           
# x_values = range(len(months))
# ax1.plot(x_values, visits_per_month, marker='o')
# ax1.set_xlabel("Month")
# ax1.set_ylabel("Visits Per Month")
# ax1.set_xticks(x_values)
# ax1.set_xticklabels(months)
# ax1.title.set_text('Monthly Visito

# age_sex.plot(kind = 'bar', figsize =(15, 10), title = 'Mental Health', legend=True)
#plt.show()