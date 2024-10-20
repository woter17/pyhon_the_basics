import os
from fileinput import filename

import requests
from fake_useragent import FakeUserAgent

main_dir = 'img'
main_page_dir = os.path.join(main_dir,'main_page')
episodes_dir = os.path.join(main_dir, 'episodes')

def download_img(url: str, path: str):
    response_data = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response_data.content)




headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://rickandmortyapi.com',
    'priority': 'u=1, i',
    'referer': 'https://rickandmortyapi.com/',
    'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': FakeUserAgent().random,
}

json_data = {
    'query': '\n    query randomCharacters($ids: [ID!]!) {\n      charactersByIds(ids: $ids) {\n        id\n        name\n        status\n        species\n        image\n        episode {\n          name\n          id\n        }\n        location {\n          name\n          id\n        }\n      }\n    }\n  ',
    'variables': {
        'ids': [
            209,
            226,
            444,
            498,
            322,
            105,
        ],
    },
}

response = requests.post('https://rickandmortyapi.com/graphql', headers=headers, json=json_data)
json_data = response.json().get('data', {}).get('charactersByIds', {})

#nahodim id episodov
episodes_ids = []
for elem in json_data:
    episodes_lst = elem['episode']
    for episode in episodes_lst:
        episodes_ids.append(episode['id'])
#ybiraem povtornie
episodes_ids = list(set(episodes_ids))
print(len(episodes_ids))



episode_url = 'https://rickandmortyapi.com/api/episode/'

for  episodes_id in episodes_ids:
    k=0
    character_urls = []
    # создание директории
    episodes_temp_dir = os.path.join(episodes_dir, episodes_id)
    os.mkdir(episodes_temp_dir)
    # нахождение url персов по эпизоду
    response = requests.get(f'{episode_url}{episodes_id}')
    json_episode_data = response.json()
    for character_url in json_episode_data['characters']:
        character_urls.append(character_url)

    character_urls = list(set(character_urls))
    for character_url in character_urls:
        k+=1
        # выгрузка картинок
        response = requests.get(character_url)
        image_src = response.json()['image']
        filename = os.path.join(episodes_temp_dir, image_src.split('/')[-1])
        download_img(url=image_src, path=filename)
        print(str(k) + ')' + 'episode ' + str(episodes_id) + ' downloaded')



#zadacha 1
# for elem in json_data:
#     img_src = elem['image']
#     filename = os.path.join(main_page_dir, img_src.split('/')[-1])
#     response = requests.get(img_src)
#     with open(filename, 'wb') as f:
#         f.write(response.content)
