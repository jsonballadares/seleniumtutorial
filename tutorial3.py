from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ChromeDriverPath = "/Users/jasonballadares/repos/seleniumtutorial/chromedriver/87.0.4280.20/chromedriver"
driver = webdriver.Chrome(ChromeDriverPath)
driver.implicitly_wait(10)
driver.get("https://orteil.dashnet.org/cookieclicker/")

bigCookie = driver.find_element_by_id("bigCookie")
cookieCount = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(bigCookie)

for i in range(5000):
    actions.perform()
    count = int(cookieCount.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.click(item)
            upgrade_actions.perform()

# driver.quit()
