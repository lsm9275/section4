import sys
import io
import os.path
import urllib.request as req
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159'
saveFile = 
