# 1 
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data
woodrankings = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
print(woodrankings.head())
steelrankings = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(steelrankings.head())
print(len(woodrankings))
print(len(steelrankings))

# 2
# Create a function to plot rankings over time for 1 roller coaster
def plot_rc_rank(rc, park, ranking):
  rc_rank = ranking[(ranking['Name'] == rc) & (ranking['Park'] == park)]
  fig, ax = plt.subplots()
  ax.plot(ranking['Year of Rank'], ranking['Rank'])
  ax.set_yticks(ranking['Rank'].values)
  ax.set_xticks(ranking['Year of Rank'].values)
  plt.title('Rankings of ' + rc + ' at ' + park)
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.show()
  plt.clf()

# 3
# Create a plot of El Toro ranking over time
plot_rc_rank('El Toro', 'Six Flags Great Adventure', woodrankings)

# Create a plot of El Toro and Boulder dash hurricanes
def plot_2_rcs(rc1, park1, rc2, park2, ranking):
  rc1ranking = ranking[(ranking['Name'] == rc1) & (ranking['Park'] == park1)]
  rc2ranking = ranking[(ranking['Name'] == rc2) & (ranking['Park'] == park2)]
  fig, ax = plt.subplots()
  ax.plot(rc1ranking['Year of Rank'],rc1ranking['Rank'], color = 'blue', label = rc1)
  ax.plot(rc2ranking['Year of Rank'],rc2ranking['Rank'], color = 'green', label = rc2)
  ax.invert_yaxis()
  plt.title('Ranking of ' + rc1 + ' vs. ' + rc2)
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.legend()
  plt.show()
  plt.clf()

plot_2_rcs('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', woodrankings)

# 4
# Create a function to plot top n rankings over time
def top_n(rankings,n):
  topn = rankings[rankings['Rank'] <= n]
  fig, ax = plt.subplots(figsize=(10,10))
  for rc in set(topn['Name']):
    rc_rankings = topn[topn['Name'] == rc]
    ax.plot(rc_rankings['Year of Rank'],rc_rankings['Rank'],label=rc)
  ax.set_yticks([i for i in range(1,11)])
  plt.title('Top ' + str(n) + ' Rankings')
  plt.xlabel('Year')
  plt.ylabel('Rank')
  plt.legend(loc='upper center')
  plt.show()
  plt.clf()  
  
# Create a plot of top n rankings over time
top_n(steelrankings, 7)
# 5
# load roller coaster data
captainc = pd.read_csv('roller_coasters.csv')
print(captainc.head())
# 6
# Create a function to plot histogram of column values
# function to plot histogram of column values
def plot_rc_histogram(df, column):
  plt.hist(df[column].dropna())
  plt.title('Histogram of Roller Coaster {}'.format(column))
  plt.xlabel(column)
  plt.ylabel('Count')
  plt.show()
  plt.clf()

# Create histogram of roller coaster speed
plot_rc_histogram(captainc, 'speed')

# Create histogram of roller coaster length
plot_rc_histogram(captainc, 'length')

# Create histogram of roller coaster number of inversions
plot_rc_histogram(captainc, 'num_inversions')

# Create a function to plot histogram of height values
def plot_rc_heights(df):
  heights = df[df['height'] <= 140]['height'].dropna()
  plt.hist(heights)
  plt.title('Roller Coaster Height')
  plt.xlabel('Height')
  plt.ylabel('Number of Coasters')
  plt.show()

# Create a histogram of roller coaster height
plot_rc_heights(captainc)
# 7
# Create a function to plot inversions by coaster at park
def numinversions(df, park):
  coasters_in_park = df[df['park'] == park]
  coasters_in_park = coasters_in_park.sort_values('num_inversions', ascending=False)
  names = coasters_in_park['name']
  numberinversions = coasters_in_park['num_inversions']
  plt.bar(range(len(numberinversions)),numberinversions)
  ax = plt.subplot()
  ax.set_xticks(range(len(names)))
  ax.set_xticklabels(names,rotation=45)
  plt.title('Number of Inversions Per Coaster at {}'.format(park))
  plt.xlabel('Roller Coaster')
  plt.ylabel('Number of Inversions')
  plt.show()
  plt.clf()
# Create barplot of inversions by roller coasters
numinversions(captainc, 'Parc Asterix')
# 8
# Create a function to plot a pie chart of status.operating
def pie_rc_status(df):
  operating = df[df['status'] == 'status.operating']
  closed = df[df['status'] == 'status.closed.definitely']
  num_operating = len(operating)
  num_closed = len(closed)
  status_counts = [num_operating,num_closed]
  plt.pie(status_counts,autopct='%0.1f%%',labels=['Operating','Closed'],colors=['blue', 'yellow'])
  plt.axis('equal')
  plt.show()
  plt.clf()
# Create pie chart of roller coasters
pie_rc_status(captainc)
# 9
# Create a function to plot scatter of any two columns
def rc_scatter(df, x, y):
  plt.scatter(df[x],df[y])
  plt.title('Scatter Plot of {} vs. {}'.format(x,y))
  plt.xlabel(x)
  plt.ylabel(y)
  plt.show()
  plt.clf()
# Create a function to plot scatter of speed vs height
rc_scatter(captainc, 'speed', 'height')
# Create a scatter plot of roller coaster height by speed
rc_scatter(captainc, 'height', 'speed')
