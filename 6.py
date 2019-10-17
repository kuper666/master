from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

num1 = browser.find_element_by_xpath('//span[@id="num1"]')
#x = num1.text
num2 = browser.find_element_by_id("num2")
#y = num2.text
summ = str(int(num1.text) + int(num2.text))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(summ) 

button3 = browser.find_element_by_xpath("//button[@type='submit']")
button3.click()
