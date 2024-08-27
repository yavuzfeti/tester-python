from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_options.add_argument("--headless")  # Arka planda çalıştırmak için bu satırı ekleyebilirsiniz

driver = webdriver.Chrome(options=chrome_options)

def instagram_login(username, password):
    driver.get('https://www.instagram.com')
    time.sleep(2)

    kullanici_adi = driver.find_element(By.NAME, 'username')
    kullanici_adi.send_keys(username)

    sifre = driver.find_element(By.NAME, 'password')
    sifre.send_keys(password)

    sifre.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.quit()

username = 'metaakdeniz'
password = ''

instagram_login(username, password)