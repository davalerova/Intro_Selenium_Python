from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
driver.maximize_window()
#sleep(5)
boton = driver.find_element_by_link_text('Tendencias')
boton.click()
sleep(5)
primeros_elementos = driver.find_element_by_id('grid-container')
nombre = primeros_elementos.find_elements_by_class_name('style-scope ytd-video-renderer')
for n in nombre:
    print(n.text)



driver.quit()