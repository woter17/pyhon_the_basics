import requests
from bs4 import BeautifulSoup

url = 'https://app.uniswap.org/'
response = requests.get(url)

# Используем BeautifulSoup для форматирования HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Сохраняем отформатированный HTML в файл
with open('uniswap.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
