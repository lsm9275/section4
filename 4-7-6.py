import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime

#조회시작날짜
start = datetime.datetime(2021,1,1)
end = datetime.datetime(2021,1,11)

gs_dji = web.DataReader('^DJI', 'stooq', start, end)

gs_spx = web.DataReader('^SPX', 'stooq', start, end)

#출력
print(gs_dji)
print(gs_spx)

#윈도우 제목
fig = plt.figure('Chart Test')

#차트 사이즈 지정
fig.set_size_inches(10,6,forward=True)

#차트설정 1
plt.plot(gs_dji.index, gs_dji['Close'], 'b', label = "DJI")

#차트설정 2
plt.plot(gs_spx.index, gs_spx['Close'], 'r', label = "SPX")

#범례 위치
plt.legend(loc='upper left')
#차트제목
plt.title('DJI & SPX')

#x축 라벨
plt.xlabel('Date')
plt.ylabel('Close')

plt.show()
