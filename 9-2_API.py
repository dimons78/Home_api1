# Добрый день, Александр!
# Направляю решение задачи №2 (на основании кода преподавателя Адилета Асанкожоева)

from pprint import pprint
import requests

with open('D:/Учеба/Нетология 2022/9_requests/Токен с Полигон.txt', encoding='utf-8') as file:
    TOKEN = file.readline().rstrip()


class YaDisk:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        # return {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files/'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        pprint(response.json())

    def _get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path: path', 'overwrite: True'}
        response = requests.get(url, params=params, headers=headers)
        return response.json().get('href')

    def upload_file(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()
        # print(response.status_code)
        if response.status_code == 201:
            print('OK')


if __name__ == '__main__':
    yadisk = YaDisk(TOKEN)
    yadisk.get_files_list()
    yadisk._get_upload_link('C:/work/Home_work_file/recipe_book1.txt')
    yadisk.upload_file('recipe_book1.txt', 'recipe_book1.txt')
