import json

data = {}
data['people'] = []
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'from':'seoul',
    'grade':[95,77,89,91]
})
data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan',
    'grade':[85,67,100,93]

})

data['people'].append({
    'name':'Lee',
    'website':'daum.net',
    'from':'Incheon',
    'grade':[98,79,99,92]
})

#json 파일 쓰기

with open('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/member.json', 'w') as outfile:
    json.dump(data, outfile)

with open('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section4/member.json', 'r') as infile:
    r = json.load(infile)
    print(type(r))
    print(r)
    print('========================')
    for p in r['people']:
        print('Name: '+p['name'])
        print('Website: '+p['website'])
        print('from: '+p['from'])
        grade = ''
        for g in p['grade']:
            grade = grade + ' ' + str(g)
        print('Grade: ', grade.lstrip())
        print('')