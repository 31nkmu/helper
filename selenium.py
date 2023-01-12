import json
import pickle
import random
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# URL = 'https://lalafo.kg/'
URL = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
IP = 'https://2ip.ru/'
INST = 'https://www.instagram.com/'

# создаем объект юзерагента
ua = UserAgent()

# создаем объект опций и добавляем в опции юзерагента
options = webdriver.ChromeOptions()
options.add_argument(
    f'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')

# отключаем режим вебдрайвера
options.add_argument('--disable-blink-features=AutomationControlled')

# включаем в фоновом режиме
options.add_argument('--headless')

# настраиваем прокси соединение
# options.add_argument(f'--proxy-server=138.128.91.65:8000')

# автоматически скачивает вебдрайвер
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# options=options)

try:
    # driver.get(INST)
    # time.sleep(3)
    # email_input = driver.find_element(By.NAME, value='username')
    # email_input.clear()
    # email_input.send_keys('k_billal_t')
    # password_input = driver.find_element(By.NAME, value='password')
    # password_input.clear()
    # password_input.send_keys('Ttt113_11qwertyyy')
    # login_click = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
    # login_click.click()
    # time.sleep(10)
    # not_now = driver.find_element(By.XPATH,
    #                               value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
    # not_now.click()
    # time.sleep(3)
    # not_now = driver.find_element(By.XPATH,
    #                               value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    # not_now.click()
    # time.sleep(5)
    #

    ## подключить куки

    # pickle.dump(driver.get_cookies(), open('cookies', 'wb'))

    driver.get(INST)
    time.sleep(3)
    for cookies in pickle.load(open('cookies', 'rb')):
        driver.add_cookie(cookies)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)



    # message = driver.find_element(By.XPATH,
    #                               value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
    # message.click()
    # time.sleep(10)
    # acc_to_message = driver.find_element(By.XPATH,
    #                                      value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/a')
    # acc_to_message.click()
    # time.sleep(5)
    # send_message = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    # send_message.send_keys('Тест')
    # send_message.send_keys(Keys.ENTER)
    # time.sleep(10)

    # driver.get(IP)
    # time.sleep(3)
    # all_category = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[1]/div/div/nav/ul/li[1]')
    # all_category.click()
    #
    # element_to_scroll = driver.find_element(By.XPATH,
    #                                         value='//*[@id="__next"]/div/div[1]/div[1]/div/div/nav/ul/li[1]/div[2]/ul/li[26]/a')
    # ActionChains(driver) \
    #     .scroll_to_element(element_to_scroll) \
    #     .perform()
    # time.sleep(3)
    # categories = all_category.find_element(by=By.XPATH,
    #                                      value='//*[@id="__next"]/div/div[1]/div[1]/div/div/nav/ul/li[1]/div[2]')
    # basic_categories = categories.find_elements(by=By.CLASS_NAME, value='main-nav__sublist-item')
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
