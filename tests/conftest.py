import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class', autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    options = [
        "--disable-search-engine-choice-screen",
        "--headless",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--remote-debugging-port=9222"
    ]

    for option in options:
        chrome_options.add_argument(option)

    # driver_path = ChromeService(executable_path='/usr/local/bin/chromedriver-mac-arm64/chromedriver')
    # driver = webdriver.Chrome(service=driver_path, options=chrome_options)
    # driver = webdriver.Chrome(options=chrome_options)

    chrome_service = ChromeService(ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver = webdriver.Remote(
        command_executor="http://admin:admin@localhost:3000",
        options=chrome_options
    )

    # Implicit wait setup for our framework
    driver.implicitly_wait(10)
    yield driver

    # Tear down
    print(f"\nTear down: chrome driver")
    driver.quit()