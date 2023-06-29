import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://artoftesting.com/samplesiteforselenium")
link = driver.find_element(By.XPATH, '//*[@id="commonWebElements"]/p[1]/a')
ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "idOfButton"))).click()
dl = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "dblClkBtn")))
ActionChains(driver).double_click(dl).perform()
WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.accept()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "male"))).click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4)")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "Performance"))).click()
Select(driver.find_element(By.ID, "testingDropdown")).select_by_value("Performance")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element(By.XPATH, '//*[@id="AlertBox"]/button').click()
WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.accept()
driver.find_element(By.XPATH, '//*[@id="ConfirmBox"]/button').click()
WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.dismiss()
time.sleep(4)
source_image = driver.find_element(By.XPATH, "//img[@alt='art of testing']")
target_textbox = driver.find_element(By.ID, "targetDiv")
time.sleep(4)
action_chains = ActionChains(driver)
action_chains.drag_and_drop(source_image, target_textbox).perform()
time.sleep(4)
driver.close()
