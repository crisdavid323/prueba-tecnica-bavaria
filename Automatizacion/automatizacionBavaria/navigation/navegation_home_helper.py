import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.show_report import Validate


class NavegationHomeHelper:
    def __init__(self, driver, is_click_buy, number_scroll):
        self.driver = driver
        self.is_click_buy = is_click_buy
        self.numberScroll = number_scroll
        self.fields_completed = {
            'email': False,
            'check_terminos_uso': False,
            'check_cookies': False,
            'btn_suscribe': False,
        }

    def scroll_home(self):
        try:
            time.sleep(5)
            # Realizar desplazamientos incrementales
            for _ in range(self.numberScroll):  # Realizar 5 desplazamientos en incrementos de 500
                self.driver.execute_script("window.scrollBy(0, 500);")
                time.sleep(3)  # Esperar un poco después de cada desplazamiento
                if self.is_click_buy:
                    try:
                        item_temp = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "")))
                        item_temp.click()

                    except TimeoutException:
                        print("No se encontró el botón de comprar")

                    _ = self.numberScroll
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error al agregar elementos al carrito: {str(e)}")

    def suscriber_email(self):
        try:
            print("Test 2")
            time.sleep(5)
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//input[contains(@class,'subscribe-email form-control')]"))).send_keys(
                    "qapruebascristhian@gmail.com")
                self.fields_completed['email'] = True
            except TimeoutException:
                self.fields_completed['email'] = False

            try:
                check_terminos_uso = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                "//div[@class='js-form-item js-form-type-checkbox checkbox form-check "
                                                "mb-3 "
                                                "js-form-item-ab-paco-subscribe-terms-conditions-and-privacy-policy "
                                                "form-item-ab-paco-subscribe-terms-conditions-and-privacy-policy']["
                                                "contains(.,'He leído, entendido y acepto los Términos de Uso del "
                                                "sitio web.')]")))
                check_terminos_uso.click()
                check_terminos_uso.is_selected()
                self.fields_completed['check_terminos_uso'] = True
            except TimeoutException:
                self.fields_completed['check_terminos_uso'] = False

            try:
                check_cookies = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                "//div[@class='js-form-item js-form-type-checkbox checkbox form-check "
                                                "mb-3 "
                                                "js-form-item-ab-paco-subscribe-agree-to-subscribe-and-receive-emails "
                                                "form-item-ab-paco-subscribe-agree-to-subscribe-and-receive-emails']["
                                                "contains(.,'Declaro que soy mayor de edad y autorizo que mis datos "
                                                "personales sean recolectados y tratados en las condiciones que se "
                                                "explican en el siguiente Aviso de Privacidad y de Cookies')]")))
                check_cookies.click()
                check_cookies.is_selected()
                self.fields_completed['check_cookies'] = True
            except TimeoutException:
                self.fields_completed['check_cookies'] = False

            try:
                item_temp = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                "//button[@data-drupal-selector='edit-ab-paco-subscribe-submit']["
                                                "contains(.,'Suscribirme')]")))
                item_temp.click()
                self.fields_completed['btn_suscribe'] = True

            except TimeoutException:
                print("No se encontró el botón de suscribir")
                self.fields_completed['btn_suscribe'] = False

            time.sleep(3)
            validator = Validate(self.fields_completed)
            validator.showValidate()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error al suscribirme: {str(e)}")
