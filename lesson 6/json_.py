import json
d = {
    'a': 1,
    'b': 2,
    'c': 3,
}
# j = json.dumps(d) #из json в str
# print(j)
# print(type(j))
# d2 = json.loads(j) #из obj python в json
# print(d2)
# print(type(d))

# with open('test.json', 'w') as f:
#     json.dump(d,f) #для файлов с записью в сам файл

with open('test.json') as f: #для достания из файла obj pyhon и перевода в json
    res = json.load(f)
    print(res)
    print(type(res))