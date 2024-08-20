import configparser


def read_config(filename='config.ini'):
    config = configparser.ConfigParser()
    config.read(filename)

    vk_user_id = config.get('vk', 'user_id', fallback=None)
    vk_screen_name = config.get('vk', 'screen_name', fallback=None)
    vk_token = config.get('vk', 'token', fallback=None)

    if not vk_token:
        raise ValueError('Не указан токен VK.')

    if not vk_user_id and not vk_screen_name:
        raise ValueError("Не указано ни 'user_id', ни 'screen_name'.")

    if vk_user_id:
        user_id_or_screen_name = vk_user_id
    else:
        user_id_or_screen_name = vk_screen_name

    folder_name = config.get('settings', 'folder_name', fallback=None)
    photo_count = config.getint('settings', 'photo_count', fallback=5)

    return {
        'user_id_or_screen_name': user_id_or_screen_name,
        'vk_token': vk_token,
        'ya_disk_token': config.get('yandex', 'token'),
        'folder_name': folder_name,
        'photo_count': photo_count
    }
