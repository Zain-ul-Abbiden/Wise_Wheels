import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager  # optional automatic install
#
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# #
driver.get("https://dev.wisewheels.com.pk/")
driver.maximize_window()
# #
# Login Hover
hover_element = driver.find_element("xpath", "//*[@id='navbarsDefault']/ul[2]/li[4]/a")
print("Test Pass")
time.sleep(2)
# #
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)
# #
#Select Login Option from Drop_Down List
driver.find_element(By.XPATH, "//nav[@role='navigation']//li[@class='nav-item dropdown no-arrow open-on-hover d-md-block d-sm-none d-none']//a[@class='nav-link'][normalize-space()='Log In']").click()
print("Test Pass 1")
time.sleep(2)
#Sign In Old Account
driver.find_element(By.NAME, "email").send_keys("Test123@yopmail.com")
driver.find_element(By.NAME, "password").send_keys("Aaasss@22")
driver.find_element(By.XPATH, "//button[normalize-space()='Log In']").click()
time.sleep(2)
print("Login Successful")

hover_element = driver.find_element("xpath", "//nav[@role='navigation']//a[@class='nav-link fw-normal font-size-16'][normalize-space()='Cars']")
print("Car Inspection")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)

wait = WebDriverWait(driver, 10)
visible_item = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//*[normalize-space(text())='Car Inspection']")))
visible_item.click()
time.sleep(2)
print("Car Comparison Done")
#==============================Car Inspection Detail==============================
driver.find_element(By.XPATH, "//body/section/div[@id='exampleModal']/div[@class='modal-dialog modal-dialog-centered modal-lg']/div[@class='modal-content']/div[@class='modal-body p-0']/div[@class='d-flex flex-column flex-lg-row rounded-xl']/div[@class='form-section p-4 d-flex flex-column justify-content-center rounded-xl']/form[@id='car-inspection-form']/div[@class='row']/div[1]/input[1]").send_keys("Audi")
time.sleep(2)
print("Make")

driver.find_element(By.XPATH, "//*[@id='model-name']").send_keys("ABC")
time.sleep(2)
print("Model")

driver.find_element(By.XPATH, "//body[1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[2]/div[1]/select[1]").click()
time.sleep(2)
print("Click Year")
wait = WebDriverWait(driver, 10)
year_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='model-year']/option[3]")))
year_option.click()
print("Year Selected")
time.sleep(2)

datetime_field = driver.find_element(By.XPATH, "//div[@role='dialog']//div//div//div//div//div//form//div//div//input[@type='datetime-local']")
datetime_field.clear()
datetime_field.send_keys("05-15-2025 03:30 PM")
time.sleep(2)
print("Date Selected")


select = Select(driver.find_element(By.ID, "city"))
time.sleep(2)
select.select_by_visible_text("Islamabad")
time.sleep(2)
print("City Selected")

driver.find_element(By.XPATH, "//div[@role='dialog']//div//div//div//div//div//form//div//div//div//input[@placeholder='Area']").send_keys("Other")
time.sleep(2)
print("Area Selected")

driver.find_element(By.XPATH, "//*[@id='car-inspection-form']/button").click()
time.sleep(2)
print("Submit Button")

