import json
from yandex_disk import YandexDisk
from vk import VK
from config import read_config


def save_to_json(saved_photos_info):
    with open('saved_photos_info.json', 'w', encoding='utf-8') as file:
        json.dump(saved_photos_info, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':

    config = read_config()

    vk_token = config['vk_token']
    user_id_or_screen_name = config['user_id_or_screen_name']
    folder_name = config['folder_name']
    photo_count = config['photo_count']

    vk = VK(vk_token, user_id_or_screen_name)

    ya_disk = YandexDisk(config['ya_disk_token'])
    ya_disk.create_folder(folder_name)
    ya_disk.save_photos_to_disk(vk, folder_name, photo_count=photo_count)
