import requests
from pages.siteMapPage import SiteMapPage
from selenium.webdriver.common.by import By


def test_links_in_sitemap(browser, homepage):
    sitemap_page: SiteMapPage = SiteMapPage(browser, homepage)
    sitemap_page.open_sitemap()
    print(f"Текущий URL = {browser.current_url}")
    all_folders: list = sitemap_page.get_all_folders()
    print(f"Количество элементов, содержащих ссылки = {len(all_folders)}")
    links: list = [folder.get_attribute("innerHTML") for folder in all_folders]
    pages_where_code_is_200 = []
    with open("don't 200.txt", 'w') as f:
        for link in links:
            print(f"Ссылка = {link}")
            r = requests.get(link)  # Проверил статус код страницы
            print(f"Статус код = {r.status_code}")
            if r.status_code != 200:
                f.write(link + " " + str(r.status_code) + "\n")
            if r.status_code == 200:
                pages_where_code_is_200.append(link)
    for page in pages_where_code_is_200:  # Итерироваться по всем страницам, которые вернули 200
        browser.get(page)
        print(f"Открытие страницы {page}")

        # Найти на странице все элементы с атрибутом rel="canonical"
        all_canonical = browser.find_elements(By.XPATH, "//link[@rel='canonical']")
        for x in all_canonical:  # Список элементов в которых содержатся каноничные ссылки
            canonical_link = x.get_attribute("href")  # Получить каноничную ссылку

            # Дальше здесь должно быть какое-то сравнение каноничной ссылки с текущей ссылкой в браузере.
            # Каким образом сравнивать URL текущей страницы (на которую сделан переход) с каноничным URL ?
            # Что является критерием сравнения,  вхождение по строке?






