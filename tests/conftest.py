import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class", autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")

    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920,1200")
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--ignore-certificate-errors")

    # chrome_options.add_argument('--dns-prefetch-disable')
    # chrome_options.add_argument('--enable-cdp-events')

    # driver_path = ChromeService(executable_path='/usr/local/bin/chromedriver-mac-arm64/chromedriver')
    # driver = webdriver.Chrome(service=driver_path, options=chrome_options)
    # driver = webdriver.Chrome(options=chrome_options)

    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Implicit wait setup for our framework
    driver.implicitly_wait(10)
    yield driver

    # Tear down
    # print(f"\nTear down: chrome driver")
    # driver.quit()