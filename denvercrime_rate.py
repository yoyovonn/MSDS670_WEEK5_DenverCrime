# Import necessary libraries.
import pandas as pd
import matplotlib.pyplot as plt
##########################################################################
# Name: Yvonne Lee
# Assignment: Using a dataset to create 3 visualizations using matplotlib.
###########################################################################
# Setting up the data directory and data frame.
data_dir = r'C:\Users\ylee_\Desktop\\'
filename = 'Denver_Crime_2001-2013.csv'
df = pd.read_csv(data_dir + filename)
columns = list(df.columns)
dpi = 300

# To check if the data frame looks right.
print(df)

################################################
# Graphing the first line graph.
# Limiting the rows that I want to include.
df1 = df.iloc[:8]
new_df = pd.DataFrame(df1.mean().to_dict(),index=[df1.index.values[-1]])
columns2 = list(new_df.columns)

x = columns2
y = new_df.iloc[0]

# Initialize.
fig, ax = plt.subplots(figsize=(9, 10))

# Setting up the chart.
ax.bar(x, y)
ax.set_title('Average Rate of Top 8 Crimes in Denver From 2001 to 2013')
ax.set_xlabel('Year')
ax.set_xticklabels(columns2)
ax.set_ylabel('Crime Average', fontsize=12, labelpad=1.5)

# Display.
plt.show()

# Save file.
plot1_filename = 'AverageRate.png'
fig.savefig(data_dir + plot1_filename, dpi=dpi)

################################################
# Graphing Crime Index for each Year
# Making a new data frame to make it easier.
df2 = pd.DataFrame({
    'Year': ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013'],
    'Index': [434.6, 446.7, 482, 532, 558.5, 477.4, 398.4, 341.2, 351.7, 336.7, 373.3, 374.6, 381.6]
})

# Initialize and set axes.
labels = ['Crime Index']
x = df2['Year']
y = df2['Index']

fig, ax = plt.subplots(figsize=(9, 10))

# Setting up the chart.
handles = ax.plot(x, y)
ax.set_title('Crime Index in Denver from 2001 to 2013')
ax.set_xlabel('Year')
ax.set_xticklabels(df2['Year'])
ax.set_ylabel('Crime Index', fontsize=12, labelpad=1.5)

# Creating the legend.
ax.legend(handles, labels, loc='upper right')
plt.show()

# Save file.
plot2_filename = 'CrimeIndex.png'
fig.savefig(data_dir + plot2_filename, dpi=dpi)

###############################################
# Graphing Comparison Between 2001 and 2013
# Limiting the rows I want to include.
df3 = df.iloc[:8]
labels = ['2001', '2013']

# Setting axes.
x = list(df3['Type'].index)
y = df3[['2001', '2013']]

fig, ax = plt.subplots(figsize=(9, 10))

# Creating chart and legend.
handles = ax.plot(x, y)
ax.set_title('Crime Rate in Denver in 2001 vs. 2013')
ax.set_xlabel('Type of Crime')
ax.set_xticklabels(df3['Type'])
ax.set_ylabel('Frequency', fontsize=12, labelpad=1.5)
ax.legend(handles, labels, loc='upper right')

# Display.
plt.show()

# Save file.
plot3_filename = '2001vs2013.png'
fig.savefig(data_dir + plot3_filename, dpi=dpi)