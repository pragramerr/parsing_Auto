import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()  # Открываем браузер
browser.get("https://auto.ru/")  # Открываем Озон в браузере

## Выбираем автомобиль Лада##
FILTER_lada = '//*[@id="LayoutIndex"]/div/div/div[1]/div/div[1]/div[3]/div/div[2]/a[1]'
filter_l = browser.find_element(by=By.XPATH, value=FILTER_lada)
filter_l.click()

time.sleep(3) ## Подождем прогрузки страницы


## Выбираем Лады в кредит##
FILTER_credit = 'on_credit'
filter_credit_on = browser.find_element(by=By.NAME, value=FILTER_credit)
filter_credit_on.click()

time.sleep(3) ## Подождем прогрузки страницы

## Жмем "Показать" ##
FILTER_button = 'ButtonWithLoader__content'
filter_button_on = browser.find_element(by=By.CLASS_NAME, value=FILTER_button)
filter_button_on.click()

time.sleep(3) ## Подождем прогрузки страницы

## Парсим название и цену ##
auto = 'ListingItem__description'
elements = browser.find_elements(by=By.CLASS_NAME, value=auto)
cars = []    #храним машины название+цена
i = 0
for element in elements:
    model = element.find_element(by=By.TAG_NAME, value="a").text  # Модель машины
    price = element.find_element(by=By.CLASS_NAME, value='ListingItemPrice__content').text.replace('₽', '').replace(' ', '') # цена без лишних 0 и значка ₽
    int(price)
    cars.append([])# новая строка
    cars[i].append(model) # добавляем марку
    cars[i].append(price)  # добавляем цену
    i += 1        #счетчик ++

cars.sort(key=lambda x: x[1]) # сортируем по цене
print(f"Модель машины: {cars[0][0]} цена: {cars[0][1]} ₽")
browser.close()