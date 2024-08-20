import requests
from tqdm import tqdm
from datetime import datetime


class YandexDisk:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'OAuth {self.token}'}

    def create_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': folder_name}
        response = requests.put(url, headers=self.headers, params=params)
        if response.status_code == 201:
            print(f"Папка '{folder_name}' успешно создана.")
        elif response.status_code == 409:
            print(f"Папка '{folder_name}' уже существует.")
        else:
            print(f"Ошибка при создании папки '{folder_name}': {response.status_code}")
        return response.status_code

    def upload_file(self, folder_name, file_name, file_url):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            'path': f'{folder_name}/{file_name}',
            'url': file_url,
            'disable_redirects': 'true'
        }
        response = requests.post(url, headers=self.headers, params=params)
        if response.status_code == 202:
            print(f"Файл '{file_name}' успешно загружен.")
        else:
            print(f"Ошибка при загрузке файла '{file_name}': {response.status_code}")
        return response.status_code

    def save_photos_to_disk(self, vk, folder_name, photo_count=5):
        data = vk.photos_info(count=photo_count)
        if 'response' not in data:
            print('Ошибка при получении данных от API VK.')
            print('Ответ API VK: ', data)
            return

        photos = data['response']['items']
        saved_photos_info = []

        for photo in tqdm(photos[:photo_count]):
            likes = photo['likes']['count']
            date = datetime.fromtimestamp(photo['date']).strftime('%Y-%m-%d_%H-%M-%S')
            file_name = f'{likes}.jpg'

            if any(saved_photo['file_name'] == file_name for saved_photo in saved_photos_info):
                file_name = f'{likes}_{date}.jpg'

            max_size_url, max_size_type = vk.get_max_size_photo(photo['sizes'])
            self.upload_file(folder_name, file_name, max_size_url)
            saved_photos_info.append({
                'file_name': file_name,
                'size': max_size_type
            })
            print(f'Сохранено фото: {file_name}, размер: {max_size_type}')
