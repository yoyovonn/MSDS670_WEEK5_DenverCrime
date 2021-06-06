import os

import pandas as pd
import matplotlib.pyplot as plt

data_dir = r'C:\Users\ylee_\Desktop\\'
filename = 'Denver_Crime_2001-2013.csv'
df = pd.read_csv(data_dir + filename)
columns = list(df.columns)

#print(df)

# Graphing the first line graph.
# df1 = df.iloc[:8]
# labels = ['Type of Murder']
#
# x = list(df1['Type'].index)
# y = df1['Average'].values
#
# fig, ax = plt.subplots(figsize=(9, 10))
#
# handles = ax.plot(x, y)
# ax.set_title('Average Rate of Specific Crimes in Denver')
# ax.set_xlabel('Type of Crime')
# ax.set_xticklabels(list(df1['Type']))
# ax.set_ylabel('Crime Average', fontsize=12, labelpad=1.5)
#
# ax.legend(handles, labels, loc='upper right')
# plt.show()

# Graphing Crime Index for each Year
# df2 = pd.DataFrame({
#     'Year': ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013'],
#     'Index': [434.6, 446.7, 482, 532, 558.5, 477.4, 398.4, 341.2, 351.7, 336.7, 373.3, 374.6, 381.6]
# })
#
# labels = ['Crime Index']
# x = df2['Year']
# y = df2['Index']
#
# fig, ax = plt.subplots(figsize=(9, 10))
#
# handles = ax.plot(x, y)
# ax.set_title('Crime Index from 2001 to 2013')
# ax.set_xlabel('Year')
# ax.set_xticklabels(df2['Year'])
# ax.set_ylabel('Crime Index', fontsize=12, labelpad=1.5)
#
# ax.legend(handles, labels, loc='upper right')
# plt.show()
#
# Graphing Comparispn Between 2001 and 2013
df3 = df.iloc[:8]
labels = ['2001', '2013']

x = list(df3['Type'].index)
y = df3[['2001', '2013']]

fig, ax = plt.subplots(figsize=(9, 10))

handles = ax.plot(x, y)
ax.set_title('Crime Rate for 2001 and 2013')
ax.set_xlabel('Type of Crime')
ax.set_xticklabels(df3['Type'])
ax.set_ylabel('Frequency', fontsize=12, labelpad=1.5)
ax.legend(handles, labels, loc='upper right')
plt.show()
