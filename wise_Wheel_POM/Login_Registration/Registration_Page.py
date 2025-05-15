from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    name_input = (By.NAME, "name")
    phone_input = (By.NAME, "phone")
    email_input = (By.NAME, "email")
    password_input = (By.NAME, "password")
    password_confirm_input = (By.ID, "passwordConfirmation")
    accept_terms_checkbox = (By.NAME, "accept_terms")
    signup_button = (By.ID, "signupBtn")

    def enter_register_details(self, name, phone, email, password):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_confirm_input).send_keys(password)
        self.driver.find_element(*self.accept_terms_checkbox).click()

    def submit_registration(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.signup_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
        try:
            button.click()
        except:
            self.driver.execute_script("arguments[0].click();", button)
