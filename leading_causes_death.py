# leading causes of death 
# using data set from data.gov
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('env/NCHS_-_Leading_Causes_of_Death__United_States.csv')

#print (df.head())
#print (df.info())
total_df = df[df['113 Cause Name'] == 'All Causes']

#print(total_df.head(10))
#print(total_df.info())
death_years_df = total_df[['Year', 'State', 'Deaths']]

def by_state_df(data_frame, state):
  by_state_df = death_years_df[data_frame.State == state]
  by_state_df.sort_values(['Year'],  inplace=True)
  by_state_df.set_index('Year')
  return by_state_df

# 'Colorado'
# print(by_state_df.head(10))
# print(by_state_df.info())
co_df = by_state_df(death_years_df, 'Colorado')
co_df.plot.line(x='Year', y='Deaths',marker='o', title = 'Deaths In Colorado' )
#ax.plot(kind = 'line', figsize =(10, 6), title = 'Deaths In Colorado',  legend=True)
plt.show()