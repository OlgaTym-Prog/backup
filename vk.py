import requests


class VK:
    def __init__(self, access_token, user_id_or_screen_name, version='5.131'):
        self.token = access_token
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

        if user_id_or_screen_name.isdigit():
            self.user_id = int(user_id_or_screen_name)
        else:
            self.screen_name = user_id_or_screen_name
            self.user_id = self.get_user_id_from_screen_name(self.screen_name)

    def get_user_id_from_screen_name(self, screen_name):
        url = 'https://api.vk.com/method/users.get'
        params = {
            'user_ids': screen_name,
            'fields': 'id'
        }
        response = requests.get(url, params={**self.params, **params})
        data = response.json()
        if 'response' in data and len(data['response']) > 0:
            return data['response'][0]['id']
        else:
            raise ValueError("Не удалось получить идентификатор пользователя.")

    def photos_info(self, album_id='profile', count=5):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': self.user_id,
            'album_id': album_id,
            'extended': 1,
            'photo_sizes': 1,
            'count': count
        }
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def get_max_size_photo(self, sizes):
        max_size_photo = max(sizes, key=lambda size: size['height'] * size['width'])
        return max_size_photo['url'], max_size_photo['type']
