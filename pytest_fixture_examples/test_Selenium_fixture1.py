from selenium.webdriver.common.by import By


def test_verifyTitle(init_browser):

    actual_title = driver.title
    assert actual_title == "Facebook – log in or sign up"


def test_verifyUrl(init_browser):

    actual_url = driver.current_url
    assert actual_url == "https://www.facebook.com/"


def test_verifyHomepageText(init_browser):

    expected_text = "Facebook helps you connect and share with the people in your life."
    actual_text = driver.find_element(By.CLASS_NAME, "_8eso").text
    assert actual_text == expected_text


def test_verifyForgottenpassword(init_browser):

    expected_fp_text = "Forgotten password?"
    actual_fp_text = driver.find_element(By.PARTIAL_LINK_TEXT, "word?").text
    assert actual_fp_text == expected_fp_text
