import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe)
time.sleep(2)
source = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[1]/img')
target = driver.find_element(By.XPATH, '//*[@id="trash"]')
action = ActionChains(driver)
action.drag_and_drop(source, target).perform()
driver.switch_to.default_content()
driver.close()
