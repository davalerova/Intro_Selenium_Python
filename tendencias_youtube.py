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
primeros_elementos = driver.find_elements_by_css_selector('#video-title > yt-formatted-string')
autor = driver.find_elements_by_xpath('//*[@id="text"]/a')
for i in  range(len(primeros_elementos)):
    print(primeros_elementos[i].text, autor[i].text)


driver.quit()