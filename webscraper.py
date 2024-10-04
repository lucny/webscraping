# https://realpython.com/beautiful-soup-web-scraper-python/
# Modul requests (pip install requests)
import requests
# Import knihovny BeautifulSoup4 (pip install beautifulsoup4), která usnadňuje web scraping
from bs4 import BeautifulSoup

# Konstanta obsahující adresu webu, z něhož chceme získávat data
# Žebříček 250 nejlépe hodnocených filmů podle serveru imdb.com
URL = 'https://www.imdb.com/chart/top'

# Odeslání požadavku metodou get na určenou URL adresu - HTTP server vrací zpět obsah stránky
page = requests.get(URL, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
# page = requests.get(URL)
# Vytvoření objektu parseru stránky
soup = BeautifulSoup(page.content, 'html.parser')
# Získání názvů filmů
titles = [tag.text.split('. ')[1] for tag in soup.select('.ipc-metadata-list-summary-item h3.ipc-title__text')]
# print(titles)
# Získání roků vzniku filmů
years = [tag.text for tag in soup.select('.ipc-metadata-list-summary-item .cli-title-metadata>.cli-title-metadata-item:nth-child(1)')]
# print(years)
lengths = [tag.text for tag in soup.select('.ipc-metadata-list-summary-item .cli-title-metadata>.cli-title-metadata-item:nth-child(2)')]
# print(lengths)
ratings = [tag.text for tag in soup.select('.ipc-metadata-list-summary-item .ipc-rating-star--rating')]
# print(ratings)
# Odkazy na detaily filmů
urls = [f'https://www.imdb.com{tag["href"]}' for tag in soup.select('.ipc-metadata-list-summary-item a.ipc-title-link-wrapper')]
# print(urls)
# Kontrolní výpis získaných údajů

for i in range(0, len(titles)):
    detail_page = requests.get(urls[i], headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    dsoup = BeautifulSoup(detail_page.content, 'html.parser')
    content = dsoup.select('[data-testid=plot]>span[data-testid=plot-xs_to_m]')
    print(f'{i + 1};{titles[i]};{years[i]};{ratings[i]};"{urls[i]}";{content[0].text}')
