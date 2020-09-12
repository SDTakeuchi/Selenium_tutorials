#python selenium tutorial #3 / tech with tim ----------20.07.29------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
#main = driver.find_elements_by_id("main")s
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    time.sleep(10)

    driver.back()
    driver.back()
    driver.back()

    time.sleep(10)

    driver.forward()
    driver.forward()

    time.sleep(5)

    driver.quit()
except:
    driver.quit()


# if you search a/th in search box first type "driver.clear()" to CLEAR everything in the search box not duplicate, append words.
