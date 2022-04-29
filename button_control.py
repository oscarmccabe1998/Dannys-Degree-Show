import RPi.GPIO as GPIO
from selenium import webdriver
from selenium.webdriver.common.by import By

import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/order_taking")

while True:
    starter_buttonState = GPIO.input(11)
    main_buttonState = GPIO.input(16)
    desert_buttonState = GPIO.input(18)

    if starter_buttonState == False:
       link =  driver.find_element_by_class_name('serveStarter')
       link.click()
       time.sleep(0.5)
    elif starter_buttonState == True:
        pass
    if main_buttonState == False:
        link = driver.find_element_by_class_name('serveMain')
        link.click()
        time.sleep(0.5)
    elif main_buttonState == True:
        pass
    if desert_buttonState == False:
        link = driver.find_element_by_class_name('serveDesert')
        link.click()
        time.sleep(0.5)
    elif desert_buttonState == True:
        pass