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
print("Auction")
time.sleep(2)
# #
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)
#Select Login Option from Drop_Down List
wait = WebDriverWait(driver, 10)
visible_item = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//*[normalize-space(text())='Auction Sheet Verification']")  # Exact visible text
))
visible_item.click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='chasis-number']").send_keys("Test")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@onclick='navigateToAuctionReport()']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//th[@scope='row']").click()
time.sleep(2)
#================================Your Detail Screen==============================
driver.find_element(By.XPATH, "//input[@id='cnic']").send_keys("345678")
time.sleep(2)
num = driver.find_element(By.XPATH, "//input[@id='jazzcash-number']")
num.clear()
time.sleep(2)
num.send_keys("03123456789")
submit_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_btn)
time.sleep(1)
submit_btn.click()
print("Detail Entered")
time.sleep(5)

try:
	# Try to find the "Payment Failed" message
	failure_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Payment Failed']")

	# If element is found, go to Dashboard
	if failure_message.is_displayed():
		print("Payment failed, navigating to Dashboard...")
		dashboard_button = driver.find_element(By.XPATH,"//nav[@role='navigation']//div[@class='navbar-identity p-sm-0']//img[1]")  # Change this XPath as needed
		dashboard_button.click()
	else:
		print("Payment status unknown. No action taken.")

except NoSuchElementException:
	# If "Payment Failed" not found, do nothing
	print("Payment successful or still processing. Staying on current page.")