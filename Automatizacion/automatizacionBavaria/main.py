# main.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main:
    def __init__(self, driver):
        self.driver = driver

    def run(self):
        print('entro')


if __name__ == "__main__":
    # Configurar el navegador
    driver = webdriver.Chrome()
    driver.get("https://www.clubcolombia.com.co")
    driver.maximize_window()

    main = Main(driver)
    main.run()
    time.sleep(2)

    driver.quit()
