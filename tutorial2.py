from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ChromeDriverPath = "/Users/jasonballadares/repos/seleniumtutorial/chromedriver/87.0.4280.20/chromedriver"
driver = webdriver.Chrome(ChromeDriverPath)
driver.get("https://techwithtim.net")

try:
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Python Programming"))
    )
    link.click()
except:
    driver.quit()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
except:
    driver.quit()

try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "sow-button-19310003"))
    )
    button.click()
except:
    driver.quit()


# driver.quit()
