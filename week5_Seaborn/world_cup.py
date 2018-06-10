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

plt.show()