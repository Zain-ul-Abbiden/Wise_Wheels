import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from wise_Wheel_POM.Login_Registration.Login_Page import LoginPage
from wise_Wheel_POM.Login_Registration.Registration_Page import RegisterPage
from wise_Wheel_POM.Buy_Screen.Car_Find import Buy_Screen
from selenium.webdriver import ActionChains

class TestLoginRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://wisewheels.com.pk/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.register_page = RegisterPage(self.driver)

    def test_login(self):
        self.login_page.hover_on_login_menu()
        time.sleep(2)
        self.login_page.click_login_option()
        time.sleep(2)
        self.login_page.enter_login_credentials("AAA1.yopmail.com", "Aaasss@22")
        self.login_page.click_login_button()
        time.sleep(2)
        print("Login Test Passed")

    # def test_register(self):
        self.login_page.click_register_link()
        time.sleep(2)
        self.register_page.enter_register_details("Test Account", "3032341234", "Test010@yopmai.com", "Aaasss@22")
        self.register_page.submit_registration()
        time.sleep(2)
        print("Registration Test Passed")



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
