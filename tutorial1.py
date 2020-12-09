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

searchResult = driver.find_element_by_name("s")
searchResult.clear()
searchResult.send_keys("test")
searchResult.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)


finally:
    driver.quit()


driver.quit()
