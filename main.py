from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
actions = ActionChains(driver)


driver.get("https://sede.administracionespublicas.gob.es/icpplus/acOpcDirect")
submit_btn = driver.find_element_by_id("btnSubmit").click()
time.sleep(5)

select = Select(driver.find_element_by_id("form"))
select.select_by_visible_text("Castellón")
accept_btn = driver.find_element_by_id("btnAceptar")
actions.move_to_element(accept_btn)
accept_btn.click()
time.sleep(10)

select2 = Select(driver.find_element_by_id("tramiteGrupo[0]"))
select2.select_by_visible_text("AUT. DE RESIDENCIA TEMPORAL POR CIRCUNS. EXCEPCIONALES POR ARRAIGO")
cookie_close = driver.find_element_by_id("cookie_action_close_header").click()
driver.implicitly_wait(5)
accept = driver.find_element_by_css_selector("input#btnAceptar").click()
driver.implicitly_wait(10)
enter_btn = driver.find_element_by_css_selector("input#btnEntrar").click()



