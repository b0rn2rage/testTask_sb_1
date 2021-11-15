import requests
from pages.siteMapPage import SiteMapPage


def test_links_in_sitemap(browser, homepage):
    sitemap_page: SiteMapPage = SiteMapPage(browser, homepage)
    sitemap_page.open_sitemap()
    print(f"Текущий URL = {browser.current_url}")
    all_folders: list = sitemap_page.get_all_folders()
    print(f"Количество элементов, содержащих ссылки = {len(all_folders)}")
    links: list = [folder.get_attribute("innerHTML") for folder in all_folders]
    pages_where_200 = []
    with open("don't 200.txt", 'w') as f:
        for link in links:
            print(f"Ссылка = {link}")
            r = requests.get(link)  # Проверил статус код страницы
            print(f"Статус код = {r.status_code}")
            if r.status_code != 200:
                f.write(link + " " + str(r.status_code) + "\n")
            if r.status_code == 200:
                pages_where_200.append(link)
    for page in pages_where_200:
        browser.get(page)  # Перешел на саму страницу
        print(f"Открытие страницы {page}")
        all_canonical = sitemap_page.get_all_canonical()  # Собрал все элементы с атрибутом rel="canonical" в один массив
        print(f"Длина каноничных элементов = {len(all_canonical)}")
        for x in all_canonical:
            x.get_attribute("href")







