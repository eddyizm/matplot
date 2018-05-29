# leading causes of death 
# using data set from data.gov
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('env/NCHS_-_Leading_Causes_of_Death__United_States.csv')

# print (df.head(10))
#print (df.info())

total_df = df[df['113 Cause Name'] == 'All Causes']

# df_allstates = df.groupby('State')['Deaths']
# print(type(df_allstates))
#print(total_df.head(10))
#print(total_df.info())

# df[(df.month == 'March')| (df.month == 'April')]           
total_state = df[(df['113 Cause Name'] != 'All Causes') & (df['State'] == 'Colorado') ]
#print(total_state.head(15))
total_state_filter = total_state[['Year', 'Cause Name', 'Deaths']]
print(total_state_filter.head(10))

death_years_df = total_df[['Year', 'State', 'Deaths']]

def by_state_df(data_frame, state):
  by_state_df = death_years_df[data_frame.State == state]
  by_state_df.sort_values(['Year'],  inplace=True)
  by_state_df.set_index('Year')
  return by_state_df

# 'Colorado'

# print(by_state_df.info())
co_df = by_state_df(death_years_df, 'Colorado')
co_df.plot.line(x='Year', y='Deaths',marker='o', grid=True,title = 'Total Deaths In Colorado' )
print(co_df.head(20))
# ca_df = by_state_df(death_years_df, 'California')
# ca_df.plot.line(x='Year', y='Deaths',marker='o', grid=True)
plt.show()