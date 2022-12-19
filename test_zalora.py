from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import time

driver = uc.Chrome()
def test_Zalora():
    driver.get("https://www.zalora.co.id/")
    driver.maximize_window()
    assert "ZALORA Indonesia: Belanja Online" in driver.title
    driver.implicitly_wait(10)
    
    # account = driver.find_element(By.ID, "account__icon")

    # Hover = ActionChains(driver).move_to_element(account)
    # Hover.perform()

    ActionChains(driver).move_to_element((driver.find_element(By.ID, "account__icon"))).perform()
    driver.find_element(By.ID, "account-menu-login-btn").click()
    driver.find_element(By.NAME, "LoginForm[email]").send_keys("arisanggara310@gmail.com")
    driver.find_element(By.NAME, "LoginForm[password]").send_keys("Traine123")
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn--fluid fsxl btn-dark login__button']").click()
    time.sleep(10)
    driver.quit()

    