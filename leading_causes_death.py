# leading causes of death 
# using data set from data.gov
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('env/NCHS_-_Leading_Causes_of_Death__United_States.csv')
print (df.head())
# >>> s = pd.Series(np.random.randn(10**6))
# >>> s.nlargest(10)  # only sorts up to the N requested
df_removed =  df[df['Cause Name'] != 'All Causes']           
df_top = df_removed.nlargest(10,columns='Deaths')
print (df_top.info())
print (df_top.head(10))

#styling
sns.set_context('notebook', font_scale=1.0)
sns.set_palette('Set3')
sns.set_style('darkgrid')
f, ax = plt.subplots(figsize=(20,10))
ax = sns.barplot( data= df_removed ,
                   x='Cause Name',
                   y='Deaths', 
                   ci=None )
# ax = sns.boxplot( data= df_removed ,
#                    x='Cause Name',
#                    y='Deaths'
#                     )

ax.set_title('Top Causes of Deaths In the US (1999-2015)')  
# ax = sns.barplot( data= df ,
#                    x='Year',
#                    y='Deaths',
#                    ci=None )
#ax.set_title('Total Deaths In the US')  
for item in ax.get_xticklabels():
    item.set_rotation(-45)
plt.show()

''' pandas exploration
    # print (df.head(10))
    # print (df.info())
    # strip unused columns
    new_df = df[['Year','Cause Name', 'State', 'Deaths']]
    # df.groupby('Team')

    #topTen = new_df.groupby(['State', 'Year'])
    bystate_df = new_df.groupby('State')
    by_cause_df = df[['Year', 'Cause Name', 'Deaths']]
    by_cause_group = by_cause_df.groupby(['Cause Name'])
    print (by_cause_group.agg(np.size))
    #print (topTen.get_group('Alabama'))
    # grouped.agg(np.size)

    alabama = bystate_df.get_group('Alabama')
    #fig, ax = plt.subplots()
    #alabama.groupby('Cause Name').plot(x='Year', y='Deaths', ax=ax, legend=True)

    # ax2 = plt.subplot(1,1,1)
    #alabama.plot.line(x='Year', y='Deaths',marker='o',ax=ax,  grid=True,title = 'Deaths In Alabama' )

    #print (topTen.agg(np.sum))
    #fig, ax = plt.subplots()
    #df.groupby('Cause Name').plot(x='Year', y='Deaths', ax=ax, legend=False)
    plt.show()
  '''

'''
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
'''