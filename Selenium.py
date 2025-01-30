from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executablePath =r"C:\Users\rajat\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

searchBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='search']")))

searchBox.send_keys("New York")

time.sleep(4)

rows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//table[@id='example']/tbody/tr[not(contains(@style, 'display: none'))]")))


total_entries = len(rows)
print(f"Total entries found: {total_entries}")

assert total_entries == 5, f"Test failed: Expected 5 entries, but found {total_entries}."

print("Test Passed")

driver.quit()    