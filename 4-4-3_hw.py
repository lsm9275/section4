import urllib.request as req
import simplejson as json
import os.path

url = 'http://jsonplaceholder.typicode.com/comments'

urlfile = 'D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/jsonplaceholder_comments.json'
savefile = 'D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/jsonplaceholder_comments_hw.json'

if not os.path.exists(urlfile):
    req.urlretrieve(url, urlfile)

items = json.load(open(urlfile,'r',encoding='utf-8'))

with open(savefile,'w') as outfile:
    for item in items:
        outfile.write(str(item['id']))
        outfile.write(str(item['body']))