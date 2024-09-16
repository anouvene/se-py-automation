import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    options = [
        "--window-size=1920,1200",
        "--headless",
        "--disable-infobars",
        "--disable-dev-shm-usage",
        "--no-sandbox",
        "--remote-debugging-port=9222"
    ]

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    for option in options:
        chrome_options.add_argument(option)

    # driver_path = ChromeService(executable_path='/usr/local/bin/chromedriver-mac-arm64/chromedriver')
    # driver = webdriver.Chrome(service=driver_path, options=chrome_options)
    # driver = webdriver.Chrome(options=chrome_options)

    chrome_service = ChromeService(ChromeDriverManager().install())
    request.instance.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Implicit wait setup for our framework
    request.instance.driver.implicitly_wait(10)
    yield request.instance.driver

    # Tear down
    print(f"\nTear down: chrome driver")
    request.instance.driver.quit()