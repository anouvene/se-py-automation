import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures('driver')
class TestLoginError:
    def test_error_login(self, driver):
        self.driver.get("http://localhost:3000/admin/login")
        
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
    
        email_input.send_keys("test@test.fr")
        password_input.send_keys("zdadzadf")
        login_button.click()

        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-critical"))
        )
        
        assert message.text == "Invalid email or password"
# #debug 
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-search-engine-choice-screen")
# # options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--remote-debugging-port=9222")
# driver = webdriver.Chrome(options=options)
# test = TestLoginError()
# test.test_error_login(driver)