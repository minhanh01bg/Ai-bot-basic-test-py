from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# browser.get('https://instagram.com/')
browser.get('https://gmail.com')

# time.sleep(400)
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def randomChar(quantity):
    return ''.join(random.choice(string.ascii_letters) for x in range(quantity))    

# print(randomChar(5))
def register():
    surName = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input')
    surName.send_keys(randomChar(7))
    # time.sleep(4)
    name = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(randomChar(7))
    # time.sleep(3)
    strUername = randomChar(29)
    userName = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input')
    userName.send_keys(strUername)
    # time.sleep(3)
    Pass = randomChar(8)
    password = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input')
    password.send_keys(Pass)
    # time.sleep(3)
    confirmPassword = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    confirmPassword.send_keys(Pass)
    submit = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
    submit.click()
    
# register()
# def logIn():
#     username = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
#     username.send_keys('yumjnan')
#     time.sleep(4)
#     password = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input') 
#     password.send_keys('S1mple))@')
#     password.submit()
#     time.sleep(7)

# logIn()

# def notify():
#     Notnow = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
#     time.sleep(3)
#     noti = browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
#     time.sleep(7)

# notify()


# browser.get('https://facebook.com/')

# def logInFace():
#     browser = browser.find_element_by_xpath('') 