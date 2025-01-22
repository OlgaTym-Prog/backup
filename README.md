# Курсовая работа: Резервное копирование фотографий из VK на Яндекс.Диск

## Описание проекта
Данный проект предназначен для резервного копирования фотографий профиля (аватарок) пользователя социальной сети VK в облачное хранилище Яндекс.Диск. 
Программа позволяет сохранить фотографии максимального размера и хранит информацию о сохранённых фотографиях в формате JSON.

## Основные возможности
1. Получение фотографий профиля пользователя VK с помощью метода **`photos.get`**.
2. Сохранение фотографий с максимальным разрешением на Яндекс.Диск.
3. Именование фотографий на основе количества лайков. Если количество лайков одинаковое, добавляется дата загрузки.
4. Сохранение информации о фотографиях (имя файла и размер) в формате JSON.
5. Создание отдельной папки на Яндекс.Диске для хранения фотографий.
6. Возможность указать, сколько фотографий сохранять (по умолчанию — 5).
7. Прогресс-бар или логирование для отслеживания выполнения программы.

---

## Входные данные
Пользователь вводит:
1. **ID пользователя VK**.
2. **Токен доступа Яндекс.Диска** (полученный с Полигона Яндекс.Диска).

---

## Выходные данные
1. **JSON-файл** с информацией о сохранённых фотографиях:
    ```json
    [
      {
        "file_name": "34.jpg",
        "size": "z"
      }
    ]
    ```
2. **Фотографии** на Яндекс.Диске, сохранённые в созданной папке.

---

## Как запустить проект

### 1. Клонирование репозитория
Склонируйте репозиторий с проектом:
```bash
git clone <URL_репозитория>
cd <имя_папки_репозитория>
```

### 2. Установка зависимостей
Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```
Установите зависимости:
```bash
pip install -r requirements.txt
```

### 3. Получение токенов
- Токен VK: Для получения токена авторизации VK используйте **инструкцию из личного кабинета**.
- Токен Яндекс.Диска: Получите токен на **платформе разработчика Яндекс.Диска**.

### 4. Настройка параметров
Создайте файл .env в корневой директории и добавьте туда токены:
```plaintext
VK_TOKEN=<ваш_токен_ВК>
YANDEX_DISK_TOKEN=<ваш_токен_Яндекс.Диск>
```

### 5. Запуск программы
Для запуска программы выполните:
```bash
python main.py
```

При запуске программа запросит:

- ID пользователя VK.
- Количество фотографий для сохранения (по умолчанию 5).
  
## Пример JSON-выхода
Программа создаёт файл **`saved_photos_info.json`** с информацией о сохранённых фотографиях. 

Пример содержимого:
```json
[
  {
    "file_name": "154_likes.jpg",
    "size": "z"
  },
  {
    "file_name": "200_likes_2023-01-01.jpg",
    "size": "y"
  }
]
```

## Используемые технологии
- Python 3.8+
- REST API VK и Яндекс.Диска
- Библиотеки:
  - requests — для взаимодействия с API.
  - tqdm — для отображения прогресс-бара.
  - python-dotenv — для работы с токенами через файл .env.
  - logging — для логирования работы программы.
