from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('week5_Seaborn/WorldCupMatches.csv')

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
# print (df.head())
# print(df.info())
#set styles
sns.set_style("whitegrid")
sns.set_context('poster', font_scale=0.5)

f, ax = plt.subplots(figsize=(30,10))
ax = sns.barplot( data= df ,
                   x='Year' ,
                   y='Total Goals'
                  )
ax.set_title('Total Goals by year')                  

df_goals = pd.read_csv('week5_Seaborn/goals.csv')
#print(df_goals.head())
f, ax2 = plt.subplots(figsize=(30,10))
sns.set_context('notebook', font_scale=1.75)
#sns.set_palette('Spectral')
ax2 = sns.boxplot(data=df_goals, x = 'year', y = 'goals', palette='Spectral')
ax2.set_title('Total Goals by Year')
plt.show()