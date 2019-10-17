from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")




x_element = browser.find_element_by_id("input_value")
x = int(x_element.text)
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

element = browser.find_element_by_id("answer")
element.send_keys(y)

button = browser.find_element_by_id("robotCheckbox")
button.click()

button1 = browser.find_element_by_id("robotsRule")
button1.click()

button3 = browser.find_element_by_xpath("//button[@type='submit']")
button3.click()
