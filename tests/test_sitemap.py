import requests
from bs4 import BeautifulSoup


def test_links_in_sitemap():
    r = requests.get("https://www.cybersport.ru/sitemap.xml")  # URL сайта, который будет тестироваться
    xml = r.text

    soup = BeautifulSoup(xml)
    sitemap_tags = soup.find_all("sitemap")  # Ищем все элементы sitemap с XML страницы
    print(f"Количество sitemap элементов =  {len(sitemap_tags)}")

    links_on_another_sitemaps = [sitemap.findNext("loc").text for sitemap in sitemap_tags]  # Здесь все sitemap с сайта

    with open("don't 200.txt", 'w') as f:
        for sitemap in links_on_another_sitemaps:
            r2 = requests.get(sitemap)
            xml2 = r2.text
            soup2 = BeautifulSoup(xml2)
            url_tags = soup2.find_all("url")
            print(f"Количество url элементов на этой sitemap {len(url_tags)}")

            url_on_this_sitemap = [url.findNext("loc").text for url in url_tags]  # Здесь все URL с определенной sitemap

            for url in url_on_this_sitemap:
                r3 = requests.get(url)
                print(f"Делаем GET запрос по URL = {url}")
                if r3.status_code != 200:  # Если статус код != 200, то записать в файл
                    f.write(url + " " + str(r3.status_code) + "\n")
                if r3.status_code == 200:   # Если 200, то распарсить html странички и найти все каноничные ссылки
                    soup3 = BeautifulSoup(r3.text, "html.parser")
                    results = soup3.findAll("link", {"rel": "canonical"})
                    print(f"Список всех элементов со страницы, в которых были найдены тэг rel='canonical' = {results}")
                    for result in results:
                        canonical_link = result.get("href")  # Получить каноничную ссылку из элемента
                        assert url == canonical_link, "Каноничная ссылка != текущему URL"






