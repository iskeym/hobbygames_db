from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3

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

        try:
            title = driver.find_element(By.XPATH, "//div[@class='product-info__main']//h1").text
            price = driver.find_element(By.CLASS_NAME, "price").text.replace(' ₽', '')
            article = driver.find_element(By.XPATH, "//div[@class='product-info__article--id']").text.replace('Код товара: ', '')
            availability = driver.find_element(By.XPATH, "//div[@class='price-card__text']").text
        except:
            title = driver.find_element(By.XPATH, "//div[@class='product-info__main']//h1").text
            price = driver.find_element(By.CLASS_NAME, "price").text.replace(' ₽', '')
            article = driver.find_element(By.XPATH, "//div[@class='product-info__article--id']").text.replace('Код товара: ', '')
            availability = 'в наличии'
        total.append((title, price, article, availability, link))

def save(total):
    conn = sqlite3.connect('myDataBase.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO games VALUES (?,?,?,?,?)', total)
    conn.commit()
    conn.close()

def parser():
    driver = webdriver.Chrome()

    links = []
    link(driver, links)

    total = []
    info(driver, links, total)

    save(total)

    driver.close()

parser()