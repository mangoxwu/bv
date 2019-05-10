import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

id_file_path = "../data/cailiaoid.csv"

 
 
driver = webdriver.Chrome()
driver.get("https://materialsproject.org/materials/mp-1175463/")
delay = 10

element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#final-structures > div.structures.pull-down > header > div.download-cif > div > button')))

element.click()

download_btn = driver.find_element_by_css_selector('#final-structures > div.structures.pull-down > header > div.download-cif > div > ul > li:nth-child(1) > a')

download_btn.click()