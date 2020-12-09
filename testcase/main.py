import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            "/Users/jasonballadares/repos/seleniumtutorial/chromedriver/87.0.4280.20/chromedriver"
        )
        self.driver.get("http://www.python.org")

    def tearDown(self):
        self.driver.close()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()


if __name__ == "__main__":
    unittest.main()