from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

element = browser.find_element_by_id("answer")
element.send_keys(y)

button = browser.find_element_by_css_selector("[for='robotCheckbox']")
button.click()

button1 = browser.find_element_by_id("robotsRule")
button1.click()

button3 = browser.find_element_by_xpath("//button[@type='submit']")
button.click()
