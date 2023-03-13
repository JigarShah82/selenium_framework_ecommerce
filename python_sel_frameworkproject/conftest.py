import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options as ChOptions
import allure


@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'edge']
    browser = os.environ.get('BROWSER')
    if not browser:
        raise Exception("The environment variable 'BROWSER' is not set.")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"This Browser {browser} is not supported"
                        f"Supported Browsers are {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif browser in 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()
    elif browser in 'headlesschrome':
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

    request.cls.driver = driver
    yield
    driver.quit()


### For: generating only pytest-html report with screenshot
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         #extra.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#
#         #check if test failed
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # checking if it is a front end test or backend test by checking if init_driver is in item.fixturenames
#             is_frontend_test = True if 'init_driver' in item.fixturenames else False
#             if is_frontend_test:
#                 results_dir = os.environ.get("RESULTS_DIR")
#                 if not results_dir:
#                     raise Exception("Environment Variable RESULTS_DIR must be set")
#                 screen_shot_name = os.path.join(results_dir, item.name + '.png')
#                 driver_fixture = item.funcargs['request']
#                 driver_fixture.cls.driver.save_screenshot(screen_shot_name)
#                 extra.append(pytest_html.extras.image(screen_shot_name))
#         report.extra = extra

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":

        xfail = hasattr(report, "wasxfail")

        #check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            # checking if it is a front end test or backend test by checking if init_driver is in item.fixturenames
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR")
                if not results_dir:
                    raise Exception("Environment Variable RESULTS_DIR must be set")
                screen_shot_name = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs['request']
                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
                              name = 'screeshot',attachment_type=allure.attachment_type.PNG)