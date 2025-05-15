import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager  # optional automatic install
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://dev.wisewheels.com.pk/")
time.sleep(2)
driver.maximize_window()

driver.find_element(By.XPATH, "//img[@alt='Mitsubishi']").click()
time.sleep(2)

#Price Low to High
driver.find_element(By.XPATH, "//div[@class='nice-select niceselecter select-sort-by small']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[contains(text(),'Price : Low to High')]").click()
time.sleep(2)
print("Price Low to High")

#Filteration
driver.find_element(By.XPATH, "//a[normalize-space()='']//i[@class='fa-solid fa-list']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='']//i[@class='fa-solid fa-bars']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//i[@class='bi bi-grid-fill']").click()
time.sleep(3)

#Price High To Low
driver.find_element(By.XPATH, "//div[@class='nice-select niceselecter select-sort-by small']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[contains(text(),'Price : High to Low')]").click()
time.sleep(2)
print("Price High To Low")
#Relevance
driver.find_element(By.XPATH, "//div[@class='nice-select niceselecter select-sort-by small']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[contains(text(),'Relevance')]").click()
time.sleep(2)
print("Relevance")
#Date
driver.find_element(By.XPATH, "//div[@class='nice-select niceselecter select-sort-by small']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[contains(text(),'Date')]").click()
time.sleep(2)
print("Date")


driver.get("https://dev.wisewheels.com.pk/")
time.sleep(5)

wait = WebDriverWait(driver, 10)

# Find all card anchors (you can refine locator if needed)
cards = driver.find_elements(By.CSS_SELECTOR, "a.border.rounded.p-1")

for i in range(len(cards)):
    # Re-fetch card elements after going back
    cards = driver.find_elements(By.CSS_SELECTOR, "a.border.rounded.p-1")
    card = cards[i]

    # Scroll card into center view using JS
    driver.execute_script("""
        arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
    """, card)

    time.sleep(1)  # Wait for scroll animation to finish
    # Wait until clickable and click
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.border.rounded.p-1")))
    card.click()
    time.sleep(2)  # Stay on detail screen for 2 seconds
    driver.back()  # Go back to cards list
print("All Car's Card are Selected")