import simplejson as json

#dict(json 선언)
data = {}
data['people'] = []
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'from':'seoul'
})
data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan'
})

data['people'].append({
    'name':'Lee',
    'website':'daum.net',
    'from':'Incheon'
})
#print(data)

#Dict(Json) -> Str
e = json.dumps(data, indent=4)
#print(type(e))
#print(e)

#str -> dict(json)
d = json.loads(e)
#print(type(d))
#print(d)

with open('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/member.json', 'w') as outfile:
    outfile.write(e)

with open('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/member.json', 'r') as infile:
    r = json.loads(infile.read())
    print(type(r))
    print(r)
    for p in r['people']:
        print('name '+p['name'])
        print('website '+p['website'])
        print('From '+p['from'])
        print('')