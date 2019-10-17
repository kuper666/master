from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
browser.get("http://suninjuly.github.io/explicit_wait2.html")

buttom1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
buttom1.click()
button = browser.find_element_by_id("book")
button.click()




# button3 = browser.find_element_by_xpath("//button[@type='submit']")
# button3.click()
#
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
#
# x_element = browser.find_element_by_id("input_value")
# x = int(x_element.text)
# y = calc(x)
#
# element = browser.find_element_by_id("answer")
# element.send_keys(y)
#
# button2 = browser.find_element_by_xpath("//button[@type='submit']")
# button2.click()
#




