import sys
import io
import os.path
import urllib.request as req
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159'
rawdata = 'D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/forecast_hw.xml'

if not os.path.exists(rawdata):
     req.urlretrieve(url, rawdata)

xml = open(rawdata,'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')
#print(soup.find_all('city'))

info = {}
for location in soup.find_all('location'):
    city = location.find('city').string
    #print(city)
    weather = location.find_all('tmn')
    #print(tmns)

    if not city in info:
        info[city]=[]
        for tmn in weather:
            info[city].append(tmn.string)
        
    
with open('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/hw.txt', 'wt') as f:
    for city in info.keys():
        #print('+', city)
        f.write(str(city)+'\n')
        for n in info[city]:
            #print('-', n)
            f.write('\t'+str(n)+'\n')

