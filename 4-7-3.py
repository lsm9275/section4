import pandas_datareader.data as web
import datetime

#조회 시작 날짜
start = datetime.datetime(2021,1,1)
end = datetime.datetime(2021,1,11)

#naver 정보 호출
gs = web.DataReader('^DJI', 'stooq', start, end)
print(gs.index)
print(gs['Open'])
print(gs.ix['2018-02-13'])
print(gs.describe())

