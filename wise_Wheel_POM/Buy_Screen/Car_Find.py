from selenium.webdriver.common.by import By

class Buy_Screen:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    category_dropdown = (By.XPATH, "//*[@id='navbarsDefault']/ul[2]/li[2]")
    search_input = (By.NAME, "q")
    location_input = (By.XPATH, "//input[@id='locSearch']")
    search_button = (By.XPATH, "//button[@class='btn btn-block bg-primary text-white']")
    list_view_button = (By.XPATH, "//i[@class='fa-solid fa-list']")
    hamburger_menu = (By.XPATH, "//a[normalize-space()='']//i[@class='fa-solid fa-bars']")

    # Slider XPaths
    mileage_slider = (By.XPATH, '//div[@id="mileageRangeSlider"]//div[2]//div[1]//div[1]')
    capacity_slider = (By.XPATH, '//div[@id="capacityRangeSlider"]//div[2]//div[1]//div[1]')

    # Filter input locators
    year_from_input = (By.ID, "year_from")
    year_to_input = (By.ID, "year_to")
    filter_button = (By.CLASS_NAME, "btn btn-default btn-block")

    # Methods
    def select_category(self):
        self.driver.find_element(*self.category_dropdown).click()

    def enter_search_text(self, search_term):
        self.driver.find_element(*self.search_input).send_keys(search_term)

    def enter_location(self, location):
        self.driver.find_element(*self.location_input).send_keys(location)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def click_list_view(self):
        self.driver.find_element(*self.list_view_button).click()

    def click_hamburger_menu(self):
        self.driver.find_element(*self.hamburger_menu).click()

    def set_mileage_slider(self, value):
        slider = self.driver.find_element(*self.mileage_slider)
        self.driver.execute_script(f"arguments[0].value = {value};", slider)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", slider)

    def set_capacity_slider(self, value):
        slider = self.driver.find_element(*self.capacity_slider)
        self.driver.execute_script(f"arguments[0].value = {value};", slider)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", slider)

    def enter_year_from(self, year):
        self.driver.find_element(*self.year_from_input).send_keys(year)

    def enter_year_to(self, year):
        self.driver.find_element(*self.year_to_input).send_keys(year)

    def click_filter_button(self):
        self.driver.find_element(*self.filter_button).click()