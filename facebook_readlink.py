from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com")
#login
login=driver.find_element_by_css_selector('#email')
pass_word=driver.find_element_by_css_selector('#pass')
login_button=driver.find_element_by_css_selector('#u_0_2')
login.send_keys('adwitiya.kr@gmail.com')
pass_word.send_keys('Sum#1234')                                              
login_button.click()
driver.get("https://www.facebook.com/KaniaSchoolOfManagement/")

name=driver.find_elements_by_class_name('_4bl9')
name_text=[]
for i in (name):
     name_text.append(i.text)
eg=name_text
#id_5c7067e6dac392f00417046 > div > div:nth-child(2) > div > div._4-u2._6590._3xaf._4-u8 > div:nth-child(2) > div > div._4bl9 > div
#id_5c7067e6dac392f00417046 > div > div:nth-child(2) > div > div._4-u2._6590._3xaf._4-u8 > div:nth-child(2) > div > div._4bl9


name_text.