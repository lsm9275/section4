import pandas as pd

df = pd.read_excel('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/excel_s1.xlsx', header=0)
#print(df)

#컬럼 값 수정
#df['State'] = df['State'].str.replace(' ','|')
#print(df)

#평균컬럼 추가
df['Avg'] = df[['2003','2004','2005']].mean(axis=1).round(2)
#print(df)

df['Sum'] = df[['2003','2004','2005']].sum(axis=1).round(2)
#print(df)

#print(df[['2003','2004','2005']].max(axis=0))
df.to_excel('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/result_s1.xlsx')

