
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# set up Chrome driver
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open Google
driver.get("https://www.google.com/")

# find search box and type chair
search = driver.find_element(By.NAME, "q")
search.clear()
search.send_keys("chair")
search.send_keys(Keys.RETURN)

# wait a few seconds so results page can load
sleep(5)

# verify the search happened
assert "chair" in driver.current_url.lower() or "chair" in driver.title.lower(), \
    f"Expected 'chair' in URL or title, got URL: {driver.current_url}, title: {driver.title}"

print("Test Passed")

# close browser
driver.quit()