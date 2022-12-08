from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from yaml.loader import SafeLoader
import sys
import yaml

s=Service("/Users/nrangasa/driver/chromedriver")
import pytest




with open('/Users/nrangasa/personal/python-webdriver/web-driver/config.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)

url = data["url"]
username = data['username']
password = data['password']


def init():
    
    chrome = wd.Chrome(service=s)
    chrome.maximize_window()
    chrome.implicitly_wait(10)
    
    
    return chrome

def test_one():
    print("hello")
    chrome = init()
    open_app(chrome)
    login(chrome)
    
def open_app(chrome):
    chrome.get(url)

def login(chrome):
   
    
       
    
    

    chrome.find_element(By.CSS_SELECTOR, "div.sign-in-modal button").click()
    chrome.find_element(By.ID, "contextual-sign-in_sign-in-modal_session_key").send_keys(username)

    chrome.find_element(By.ID,"contextual-sign-in_sign-in-modal_session_password").send_keys(password)

    chrome.find_element(By.CSS_SELECTOR, "button[data-id='sign-in-form__submit-btn']").click()

    name = chrome.find_element(By.XPATH,"//section//div/h1").text

    print(name)

    assert name == 'Nandakumar Rangasamy'

    chrome.



    
    # assert chrome.g
    # chrome.close()

