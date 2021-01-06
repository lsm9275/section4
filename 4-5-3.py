import pandas as pd
import numpy as np

#랜덤 Dataframe 생성
#df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=['ONE','TWO','THREE','FOUR'])
df = pd.DataFrame(np.random.randn(100,4), columns=['ONE','TWO','THREE','FOUR'])
print(df)

df.to_csv('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/result_s2_2.csv', index=False)