from selenium import webdriver
from selenium.webdriver.common.by import By

def link(driver, links):
    url = ('https://hobbygames.ru/catalog/search?keyword=&time%5B%5D=1-15&price_to=2400&parameter_type=2805')
    driver.get(url)

    items = driver.find_elements(By.CLASS_NAME, "name-desc")
    for item in items:
        link = item.find_element(By.CLASS_NAME, "name").get_attribute('href')
        links.append(link)

        print(link)

def info(driver, links, total):
    for link in links:
        driver.get(link)

        x = []
        try:
            x.append({
                'title': driver.find_element(By.XPATH, "//div[@class='product-info__main']//h1").text,
                'price': driver.find_element(By.CLASS_NAME, "price").text.replace(' ₽', ''),
                'article': driver.find_element(By.XPATH, "//div[@class='product-info__article--id']").text.replace('Код товара: ', ''),
                'availability': driver.find_element(By.XPATH, "//div[@class='price-card__text']").text,
                'link': link
            })
        except:
            x.append({
                'title': driver.find_element(By.XPATH, "//div[@class='product-info__main']//h1").text,
                'price': driver.find_element(By.CLASS_NAME, "price").text.replace(' ₽', ''),
                'article': driver.find_element(By.XPATH, "//div[@class='product-info__article--id']").text.replace('Код товара: ', ''),
                'availability': 'в наличии',
                'link': link
            })

        print(x)
        total.extend(x)

def parser():
    driver = webdriver.Chrome()

    links = []
    link(driver, links)

    total = []
    info(driver, links, total)

    driver.close()

parser()