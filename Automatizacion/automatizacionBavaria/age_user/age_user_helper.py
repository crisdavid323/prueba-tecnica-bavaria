import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.show_report import Validate


class AgeUserHelper:
    def __init__(self, driver, si_no, is_check_remember_data):
        self.driver = driver
        self.si_no = si_no
        self.is_check_remember_data = is_check_remember_data
        self.fields_completed = {
            'check_remenber_data': False,
            'click_si': False,
            'click_no': False,
        }

    def age_user(self):
        try:
            # Seleccionar si o no para crusar la validación
            print("Test 1")
            time.sleep(10)
            if self.is_check_remember_data:
                try:
                    itemTemp = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'checkbox__control')]")))
                    itemTemp.click()
                    self.fields_completed['check_remenber_data'] = True

                except TimeoutException:
                    print("No se encontró el check de recordar mis datos")
                    self.fields_completed['check_remenber_data'] = False

            time.sleep(2)
            
            if self.si_no:
                try:
                    itemTemp = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@class='age_gate_yes'][contains(.,'Sí')]")))
                    itemTemp.click()
                    self.fields_completed['click_si'] = True

                except TimeoutException:
                    print("No se encontró el si de la edad")
                    self.fields_completed['click_si'] = False

            else:
                try:
                    itemTemp = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@class='age_gate_no'][contains(.,'No')]")))
                    itemTemp.click()
                    self.fields_completed['click_no'] = True
                    self.driver.quit()

                except TimeoutException:
                    print("No se encontró el no de la edad")
                    self.fields_completed['click_no'] = False

            validator = Validate(self.fields_completed)
            validator.showValidate()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error al escoger si es mayor de edad: {str(e)}")
