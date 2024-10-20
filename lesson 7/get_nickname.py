import requests
from fake_useragent import FakeUserAgent

cookies = {
    '_ga_2YVCQ4QDRJ': 'GS1.1.1729324178.1.0.1729324178.60.0.0',
    '_ga': 'GA1.1.987558733.1729324178',
    'ASP.NET_SessionId': 's30ovyinmxgogvacyewtmvdk',
    '_ga_MDPVTNLB3G': 'GS1.1.1729324178.1.0.1729324178.60.0.0',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.6',
    'content-type': 'application/json; charset=UTF-8',
    # 'cookie': '_ga_2YVCQ4QDRJ=GS1.1.1729324178.1.0.1729324178.60.0.0; _ga=GA1.1.987558733.1729324178; ASP.NET_SessionId=s30ovyinmxgogvacyewtmvdk; _ga_MDPVTNLB3G=GS1.1.1729324178.1.0.1729324178.60.0.0',
    'origin': 'https://spinxo.com',
    'priority': 'u=1, i',
    'referer': 'https://spinxo.com/',
    'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': FakeUserAgent().random,
    'x-requested-with': 'XMLHttpRequest',
}

json_data = {
    'snr': {
        'category': 0,
        'UserName': '',
        'Hobbies': '',
        'ThingsILike': '',
        'Numbers': '',
        'WhatAreYouLike': '',
        'Words': '',
        'Stub': 'username',
        'LanguageCode': 'en',
        'NamesLanguageID': '45',
        'Rhyming': False,
        'OneWord': False,
        'UseExactWords': False,
        'ScreenNameStyleString': 'Any',
        'GenderAny': False,
        'GenderMale': False,
        'GenderFemale': False,
    },
}

response = requests.post('https://spinxo.com/services/NameService.asmx/GetNames', headers=headers, json=json_data)
print(response.status_code)

names_temp = []
while len(names_temp) < 100:
    for name in response.json().get('d', {}).get('Names', {}):
        names_temp.append(name)
        names_temp = list(set(names_temp))
    response = requests.post('https://spinxo.com/services/NameService.asmx/GetNames', headers=headers, json=json_data)
print(names_temp)
with open('names.txt', 'w') as f:
        for i, name in enumerate(names_temp, start=1):
            f.write(str(i) + ') ' + name + '\n')
            if i == 100:
                break