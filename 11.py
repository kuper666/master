from selenium import webdriver
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button3 = browser.find_element_by_xpath("//button[@type='submit']")
button3.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_id("input_value")
x = int(x_element.text)
y = calc(x)

element = browser.find_element_by_id("answer")
element.send_keys(y)

button2 = browser.find_element_by_xpath("//button[@type='submit']")
button2.click()





