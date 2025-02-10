from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Twitter
driver.maximize_window()
driver.get("https://twitter.com")
time.sleep(1)

# Login
with open("login.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    if len(lines) == 2:
        username = lines[0].strip()
        password = lines[1].strip()
    else:
        print("login.txt does not have two lines (input username in first line and password in second line)")

button = driver.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]/ancestor::div[1]")
button.click()
time.sleep(1)
usernameElement = driver.find_element(By.XPATH, "//span[contains(text(), 'Phone, email, or username')]/ancestor::div[2]/following-sibling::div/descendant::div//input")
usernameElement.send_keys(username)
usernameElement.send_keys(Keys.ENTER)
time.sleep(1)
passwordElement = driver.find_element(By.XPATH, "//span[contains(text(), 'Password')]/ancestor::div[2]/following-sibling::div/descendant::div//input")
passwordElement.send_keys(password)
passwordElement.send_keys(Keys.ENTER)
time.sleep(3)
bookmarks = driver.find_element(By.XPATH, "//span[contains(text(), 'Bookmarks')]/ancestor::div[2]")
bookmarks.click()

# Keep the browser open for a few seconds
time.sleep(10)

# Close the browser
driver.quit()