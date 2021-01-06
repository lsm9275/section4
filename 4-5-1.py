import pandas as pd

#df = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s1.csv')
#print(df)

#df = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s1.csv', skiprows=[0])
#print(df)

#df = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s1.csv', skiprows=[0], header=None)
#print(df)

#df = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s1.csv', skiprows=[0], header=None, names=['Month', 2013,2014,2015])
#print(df)

#df = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s1.csv', skiprows=[0], header=None, names=['Month', 2013,2014,2015], index_col=[0])
#print(df)

#df = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s1.csv', skiprows=[0], header=None, names=['Month', 2013,2014,2015], index_col=[0], na_values=['JAN'])
#print(df)
#print(pd.isnull(df))

#df = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s1.csv', skiprows=[0], header=None, names=['Month', 2013,2014,2015])
#print(df)
#print(df.index)
#print(list(df.index))
#print(df.index.values)

#print(df.rename(index={0:'aa',1:'bb',2:'cc'}))
#print(df.rename(index=lambda x:x*10))

#df = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s2.csv',sep=";", skiprows=[0], header=None, names=['Name', 'Test1', 'Test2', 'Test3', 'Test4', 'Grade'])
#print(df)

#df2 = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s2.csv',sep=";", skiprows=[0], header=None, names=['Name', 'Test1', 'Test2', 'Test3', 'Test4', 'Grade'])
#df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
#print(df2)


df2 = pd.read_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/csv_s2.csv',sep=";", skiprows=[0], header=None, names=['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1)
#print(df2)

df2['sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)
print(df2)