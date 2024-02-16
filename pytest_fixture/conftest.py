import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope='package')
def init_browser():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    time.sleep(5)
    driver.close()


@pytest.fixture(scope='class')
def init_chrome(request):
    s = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=s)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture(scope='class')
def init_edge(request):
    s = Service(EdgeChromiumDriverManager().install())
    edge_driver = webdriver.Edge(service=s)
    request.cls.driver = edge_driver
    yield
    edge_driver.close()


@pytest.fixture(scope='class')
def init_firefox(request):
    s = Service(GeckoDriverManager().install())
    ff_driver = webdriver.Firefox(service=s)
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.fixture(params=['chrome', 'firefox', 'edge'], scope='class')
def init_all_browser(request):
    global web_driver
    if request.param == "chrome":
        s = Service(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=s)

    if request.param == "firefox":
        s = Service(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=s)

    if request.param == "edge":
        s = Service(EdgeChromiumDriverManager().install())
        web_driver = webdriver.Edge(service=s)

    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture
def init_chrome_browser():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.close()
