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
    options.add_argument("--headless")                      # --headless runs Chrome with no visible window. This is needed for CI environments like GitHub Actions where there is no screen.
    options.add_argument("--no-sandbox")                    # --no-sandbox and --disable-dev-shm-usage are needed to make Chrome work inside Linux containers.
    options.add_argument("--disable-dev-shm-usage")
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False} # Disable Chrome's password manager popups which can interfere with tests that involve logging in. This is done by setting some preferences in ChromeOptions.
    options.add_experimental_option("prefs", prefs)
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

# TC02 Invalid Login
def test_invalid_login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")     # targetting the error message on screen which is <h3 data-test="error">
    assert error.is_displayed()

# TC03 Add Item to Cart
def test_add_item_to_cart(driver):
    login(driver)                                                       
    driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()          # By.CSS_SELECTOR, ".btn_inventory" finds the first "Add to cart" button on the page.
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")  # By.CLASS_NAME, "shopping_cart_badge" finds the cart icon counter in the top right corner.
    assert cart_count.text == "1"                                           # cart_count.text == "1" checks that the number shown on the cart is exactly "1" after adding one item.

# TC04 Complete Checkout
def test_complete_checkout(driver):
    login(driver)
    driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()          # .btn_inventory adds the first item to the cart, same as TC03.
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()        # shopping_cart_link clicks the cart icon to go to the cart page.
    driver.find_element(By.ID, "checkout").click()                          # These are IDs of the elements on the checkout pages. Each one moves you one step forward through the checkout flow.
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("5000")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    confirmation = driver.find_element(By.CLASS_NAME, "complete-header")    # complete-header is the "Thank you for your order" text that appears on the confirmation page.
    assert confirmation.is_displayed()

# TC05 Logout
def test_logout(driver):
    login(driver)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    
    # This is the only test that uses WebDriverWait. The other tests used implicitly_wait which is a general background wait.
    # When you click the hamburger menu, the sidebar slides in with an animation. If Selenium tries to click "Logout" before the animation finishes, it will fail because the element is not clickable yet.
    # WebDriverWait(driver, 10) creates a wait object that will keep trying for up to 10 seconds.
    # Sometimes need to try increasing the wait time to give the sidebar more time to fully open before trying to click the logout link.
    wait = WebDriverWait(driver, 10)                                                     
    logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))    # wait.until(EC.element_to_be_clickable(...)) keeps checking until the logout link is actually clickable, then returns it.
    logout_link.click()
    assert driver.current_url == BASE_URL + "/"