import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {'path' : path_to_file, 'overwrite': 'true'}
        response_with_upload_link = requests.get(url, headers=headers, params=params).json()
        upload_link = response_with_upload_link.get('href')
        response = requests.put(upload_link, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Успешно загружен'
        else:
            error = f'Код ошибки: {response.status_code}'
            return error

if __name__ == '__main__':
    path_to_file = 'mem.jpg' # Файл находится в одной папке с main.py
    token = '' # Вставить токен
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
print(result)