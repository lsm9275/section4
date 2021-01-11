from pandas import Series, DataFrame
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

r_data = {'city':['서울','대구', '부산', '대전'], 'Total1':[55000, 49000, 52000, 50000], 'Total2':[65000, 59000, 62000, 60000]}
i_data = ['one',' two', 'three', 'four']

#출력
print(r_data)
print(i_data)

#dataframe 정의
d_frame = DataFrame(r_data, index=i_data)
print(type(d_frame))
print(d_frame)
print(d_frame.index)
print(d_frame.values)
print(d_frame['city'])
print(d_frame.ix['one'])
print(type(d_frame.ix['one']))

#값순회
for e in d_frame.values:
    for i, z in enumerate(e):
        print(i,z)