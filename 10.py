from selenium import webdriver
import os 

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

elements = browser.find_elements_by_css_selector('input[required]')
for element in elements:
    element.send_keys("Мой ответ")

#driver.find_element_by_name('file.txt').send_keys('C://Users/Home/selenium_env/file.txt')
current_dir = os.path.abspath(os.path.dirname(__file__)
#print (os.path.abspath(__file__))
#print (os.path.abspath(os.path.dirname(__file__)))


file_path = os.path.join(current_dir, 'file.txt')            


element = browser.find_element_by_id("file")
element.send_keys(file_path)


button3 = browser.find_element_by_xpath("//button[@type='submit']")
button3.click()
