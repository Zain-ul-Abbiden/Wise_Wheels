from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    login_menu = (By.XPATH, "//*[@id='navbarsDefault']/ul[2]/li[4]/a")
    login_option = (By.XPATH, "//nav[@role='navigation']//li[@class='nav-item dropdown no-arrow open-on-hover d-md-block d-sm-none d-none']//a[@class='nav-link'][normalize-space()='Log In']")
    email_input = (By.NAME, "email")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[normalize-space()='Log In']")
    register_link = (By.XPATH, "//a[normalize-space()='Register']")

    # Methods
    def hover_on_login_menu(self):
        hover_element = self.driver.find_element(*self.login_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()

    def click_login_option(self):
        self.driver.find_element(*self.login_option).click()

    def enter_login_credentials(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def click_register_link(self):
        self.driver.find_element(*self.register_link).click()
