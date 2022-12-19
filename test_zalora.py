from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import time

driver = uc.Chrome()
def test_Zalora():
    driver.get("https://www.zalora.co.id/") #membuka halaman zalora
    driver.maximize_window() #memperbesar windows
    assert "ZALORA Indonesia: Belanja Online" in driver.title #mengecek title dari halaman zalora
    driver.implicitly_wait(10) #menunggu proses selama 10 detik
    ActionChains(driver).move_to_element((driver.find_element(By.ID, "account__icon"))).perform() #membuka hover menu
    driver.find_element(By.ID, "account-menu-login-btn").click() #meng-klik 
    driver.find_element(By.NAME, "LoginForm[email]").send_keys("arisanggara310@gmail.com")
    driver.find_element(By.NAME, "LoginForm[password]").send_keys("Traine123")
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn--fluid fsxl btn-dark login__button']").click()
    time.sleep(10)
    driver.quit()

    