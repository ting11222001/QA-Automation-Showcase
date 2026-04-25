import pytest                                           # pytest is the test runner. It finds functions that start with test_ and runs them.
from selenium import webdriver                          # webdriver is Selenium. It controls the browser.
from selenium.webdriver.common.by import By             # By lets you find HTML elements by ID, class, CSS selector, etc.
from selenium.webdriver.chrome.service import Service   # Service and ChromeDriverManager handle the Chrome browser driver automatically. You don't have to download it manually.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait     # WebDriverWait and EC are used when you need to wait for something to appear on the page before clicking it.
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture                                             # @pytest.fixture tells pytest this function is not a test. It is setup code that other tests can use. A fixture is just a function that pytest runs automatically to set something up before a test.
def driver():                                               # The driver function is the fixture. It creates a browser, gives it to the test, then closes the browser when the test finishes. In hardware testing for example, a fixture is a physical frame that holds a device in place while you test it. In pytest, it holds your test environment in place.
    options = webdriver.ChromeOptions()                     # ChromeOptions() lets you configure the browser before opening it.
    # options.add_argument("--headless")                      # --headless runs Chrome with no visible window. This is needed for CI environments like GitHub Actions where there is no screen.
    options.add_argument("--no-sandbox")                    # --no-sandbox and --disable-dev-shm-usage are needed to make Chrome work inside Linux containers.
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())      # ChromeDriverManager().install() downloads the correct Chrome driver automatically.
    d = webdriver.Chrome(service=service, options=options)
    d.implicitly_wait(5)                                    # d.implicitly_wait(5) tells Selenium to wait up to 5 seconds when looking for an element before giving up.
    yield d                                                 # yield d passes the browser to your test. Everything after yield runs after the test finishes.
    d.quit()                                                # d.quit() closes the browser after the test is done.                 


# A helper function holds the login step that multiple tests share
def login(driver):  
    driver.get(BASE_URL)                                            # driver.get(BASE_URL) opens the browser and goes to the URL.
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)     # .send_keys(USERNAME) types the value of your USERNAME constant into that field.
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()              # .click() clicks the login button.

# TC01 Valid Login: TC01 is specifically testing the login action itself, so it makes sense to write it out fully here.
def test_valid_login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url