from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executablePath =r"C:\Users\rajat\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
time.sleep(5)
searchBox = driver.find_element(By.XPATH, "//input[@type='search']")
searchBox.send_keys("New York")
time.sleep(10)
rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr[not(contains(@style, 'display: none'))]")
total_entries = len(rows)
print(f"Total entries found: {total_entries}")
if total_entries == 5:
    print("Test Passed")
else:
    print(f"Test Failed,found{total_entries}")

driver.quit()    