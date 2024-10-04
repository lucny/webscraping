# https://realpython.com/beautiful-soup-web-scraper-python/
# Modul requests (pip install requests)
import requests
# Import knihovny BeautifulSoup4 (pip install beautifulsoup4), která usnadňuje web scraping
from bs4 import BeautifulSoup

# Konstanta obsahující adresu webu, z něhož chceme získávat data
# Žebříček 250 nejlépe hodnocených filmů podle serveru imdb.com
URL = 'https://www.csfd.cz/zebricky/filmy/nejlepsi/'

# Odeslání požadavku metodou get na určenou URL adresu - HTTP server vrací zpět obsah stránky
page = requests.get(URL, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
# page = requests.get(URL)
# Vytvoření objektu parseru stránky
soup = BeautifulSoup(page.content, 'html.parser')
title_tags = soup.select('article a.film-title-name')
titles = [tag.text.strip() for  tag in title_tags]
urls = [tag['href'] for  tag in title_tags]
years = [tag.text[1:-1] for tag in soup.select('article span.film-title-info .info')]
print(years)
for i in range(0, 5):
    detail_page = requests.get(f'https://www.csfd.cz/{urls[i]}', headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    dsoup = BeautifulSoup(detail_page.content, 'html.parser')
    plot = dsoup.select('.plot-full.hidden>p')[0].text if dsoup.select('.plot-full.hidden>p') else ""
    print(f'{i + 1};"{titles[i]}";{years[i]};"{urls[i]}";"{plot.strip()}"')