import unittest
import os

from selenium import webdriver

from age_user.age_user_helper import AgeUserHelper
from navigation.navegation_home_helper import NavegationHomeHelper


class TestMain(unittest.TestCase):
    si_no = True
    is_check_remember_data = True
    is_click_buy = False
    numberScroll = 5

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.clubcolombia.com.co")
        cls.driver.maximize_window()

    def test_1_click_initial(self):
        age_user_helper = AgeUserHelper(self.driver, self.si_no, self.is_check_remember_data)
        age_user_helper.age_user()

    def test_2_navegation(self):
        navegation_home_helper = NavegationHomeHelper(self.driver, self.is_click_buy, self.numberScroll)
        navegation_home_helper.scroll_home()
        navegation_home_helper.suscriber_email()

    # def test_3_buy_to_cart(self):

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    # Obtener la ruta absoluta del directorio de informes
    reports_dir = os.path.abspath("../reportsDoc")
