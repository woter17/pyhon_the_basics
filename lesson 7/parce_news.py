import csv  # Импортируем модуль для работы с CSV файлами
import time  # Импортируем модуль для работы с временем
import os  # Импортируем модуль для работы с файловой системой
import requests  # Импортируем модуль для выполнения HTTP-запросов
from bs4 import BeautifulSoup as BS  # Импортируем библиотеку для парсинга HTML
from fake_useragent import FakeUserAgent  # Импортируем для генерации случайного User-Agent

# URL сайта, с которого будем извлекать новости
url = 'https://www.benzinga.com/markets'
# Путь к CSV файлу, куда будем сохранять новости
path = './news.csv'
# Заголовки для имитации запроса от браузера
headers = {
    'user-agent': FakeUserAgent().random
}

def fetch_news():
    """Функция для извлечения новостей с сайта."""
    response = requests.get(url, headers=headers)  # Выполняем GET-запрос
    html = BS(response.content, 'html.parser')  # Парсим HTML-код страницы
    news_lst = html.select('.newsfeed-card.text-black')  # Выбираем элементы новостей
    news_data = []  # Список для хранения извлеченных данных

    # Проходим по каждому элементу новостей
    for new in news_lst:
        header = new.select_one('div div').text.strip()  # Извлекаем заголовок
        link = new.select_one('.post-card-article-link')['href']  # Извлекаем ссылку
        text = new.select_one('.post-card-article-link div .post-teaser').text.strip()  # Извлекаем текст новости
        news_data.append((time.strftime('%Y-%m-%d %H:%M:%S'), header, text, link))  # Добавляем данные в список

    return news_data  # Возвращаем список новостей

def save_to_csv(news_data):
    """Функция для сохранения новостей в CSV файл."""
    file_exists = os.path.isfile(path)  # Проверяем, существует ли файл

    # Читаем существующие строки, если файл существует
    existing_rows = []
    if file_exists:
        with open(path, 'r', encoding='utf-8') as f:  # Открываем файл для чтения
            reader = csv.reader(f)  # Создаем объект для чтения из CSV
            existing_rows = [tuple(row) for row in reader]  # Читаем существующие строки

    with open(path, 'a', newline='', encoding='utf-8') as f:  # Открываем файл для добавления данных
        writer = csv.writer(f)  # Создаем объект для записи в CSV

        if not file_exists:
            # Записываем заголовки, если файл новый
            writer.writerow(['Time', 'Header', 'Text', 'Link'])

        # Проходим по каждой новости
        for row in news_data:
            # Если новости нет в существующих, добавляем ее
            if row not in existing_rows:
                writer.writerow(row)  # Записываем новую строку в CSV

def main(interval):
    """Основная функция, которая запускает процесс извлечения и сохранения новостей."""
    while True:  # Бесконечный цикл
        news_data = fetch_news()  # Извлекаем новости
        save_to_csv(news_data)  # Сохраняем новости в CSV
        time.sleep(interval)  # Ждем заданный интервал времени перед следующим запросом

if __name__ == '__main__':
    # Устанавливаем интервал обновления в секундах
    update_interval = 60  # Например, 60 секунд
    main(update_interval)  # Запускаем основную функцию
