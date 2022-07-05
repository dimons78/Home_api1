
import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

names = {}

resp = requests.get(url)

for i in range(len(resp.json())):
    if resp.json()[i]['name'] == 'Hulk':
        names['Hulk'] = resp.json()[i]['powerstats']['intelligence']
    if resp.json()[i]['name'] == 'Captain America':
        names['Captain America'] = resp.json()[i]['powerstats']['intelligence']
    if resp.json()[i]['name'] == 'Thanos':
        names['Thanos'] = resp.json()[i]['powerstats']['intelligence']

# print(names)

sorted_list_file = sorted(names.items(), key=lambda x: -x[1])
# print(sorted_list_file)
print(f'Самый умный из героев: {sorted_list_file[0][0]}')
