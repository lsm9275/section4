import urllib.request as req
import simplejson as json
import os.path

#url
url = 'https://api.github.com/repositories'

#경로와 파일명
savename = 'D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/repo.json'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

items = json.load(open(savename, 'r', encoding='utf-8'))
#items = json.loads(open(savename, 'r', encoding='utf-8').read())

#출력
for item in items:
    print(item['full_name']+'   -   '+item['owner']['url'])
