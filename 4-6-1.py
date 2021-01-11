import pandas as pd
#xlrd, openpyxl

#기본 읽기1
#df = pd.read_excel('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/excel_s1.xlsx', sheet_name=0)
#print(df.head())
#print(df.tail())

#df = pd.read_excel('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/excel_s1.xlsx', skiprows=[0], skip_footer = 10)
#print(df)

#df = pd.read_excel('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/excel_s1.xlsx', header=0)
#print(df)
#print(list(df))
#print(list(df.columns.values))

#df = pd.read_excel('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/excel_s1.xlsx', skiprows=[0], header=None, names=['State',2003, 2004, 2005])
#print(df)

#df = pd.read_excel('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/excel_s1.xlsx', header=0, na_values='...', converters={'2003':lambda w: w if w > 60000 else None})
#print(df)
#df = pd.read_excel('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/excel_s1.xlsx', header=0, na_values='...', converters={'2003':lambda w: w if w > 60000 else None})
#print(df)
#print(pd.isnull(df))

df = pd.read_excel('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/excel_s1.xlsx', header=0)
print(df)
print(df.rename(index=lambda x: x+1))
print(df.rename(index=lambda x: x+1).index)