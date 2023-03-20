import pandas as pd
import numpy as np
import os
from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def element_presence(by, selector, time):
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    WebDriverWait(driver, time).until(element_present)

def element_not_presence(by, selector, time):
    element_not_present = EC.invisibility_of_element((By.CSS_SELECTOR, selector))
    WebDriverWait(driver, time).until(element_not_present)

def filter_the_contacts(filename):
    all_contacts = pd.read_csv(filename)
    all_contacts = all_contacts[["Number", "Name", "Message"]]
    all_contacts['Message'] = all_contacts['Message'].str.replace("\n", "\ue008\n\ue008")

    wishing_contacts = dict()
    
    for index, row in all_contacts.iterrows():
        print(str(row['Number'])+"  -  "+str(row['Name']))
        wishing_contacts[str(row['Number'])] = str(row['Message'])
        
    return wishing_contacts

def click_element(selector, waitTime = 10, sleepTime = 1):
    element_presence(By.CSS_SELECTOR, selector, waitTime)
    targetclick = driver.find_element(By.CSS_SELECTOR, selector)
    targetclick.click()
    sleep(sleepTime)

def send_attachment(filepath):
    click_element("span[data-icon='clip']")
    element_presence(By.CSS_SELECTOR, "input[type='file']", 10)
    attachfile = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    attachfile.send_keys(filepath)
    sleep(1)

    click_element('div[aria-label="Send"]')
    
def send_contact(cp):
    click_element("span[data-icon='clip']")
    click_element("span[data-icon='attach-contact']", 10, 3)
    click_element("div[data-testid='chat-list-search']")

    searchcontact = driver.find_element(By.CSS_SELECTOR, "div[data-testid='chat-list-search']")
    searchcontact.send_keys(cp)
    sleep(3)

    click_element('div[data-testid="cell-frame-title"]')
    click_element('span[data-icon="send"]')
    click_element('span[data-icon="send"]')


# Get the path of the current working directory
cwd = os.getcwd()

# Create a subdirectory for storing cookies
cookies_dir = os.path.join(cwd, 'cookies')

#load the contacts to be sent from the csv
massmessage = "template.csv"
sendToContacts = filter_the_contacts(massmessage)

# load webdriver
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={cookies_dir}")
options.add_argument("--headless=new")
ser = Service(r"C:/Users/Azalea/chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=options)
driver.get('https://web.whatsapp.com')

# scan the qr code and start the whatsapp
element_presence(By.CSS_SELECTOR, 'div[data-testid="chat-list-search-container"]', 3600)

# check the sync completion
click_element('span[data-testid="menu"]', 360)
click_element('div[aria-label="Settings"]')
element_not_presence(By.CSS_SELECTOR, 'span[data-icon="sync-in-progress"]', 600)
click_element('span[data-testid="back"]', 10, 5)

i=0
cp = 6285173099006

for key, value in sendToContacts.items():
    #search contact
    click_element('div[data-testid="chat-list-search"]')
    input_box = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="chat-list-search"]')
    input_box.send_keys(key)
    sleep(3)

    try:
        #click on contact result
        try:
            click_element('div[data-testid="cell-frame-title"]')
        
        except:
            print(key + " is not found")
            try:
                click_element("span[data-icon='x-alt']", 10, 30)
                continue
            except:
                sleep(30)
                continue

        #send text message 
        try:
            #click on message box
            click_element('div[data-testid="conversation-compose-box-input"]')

            #type text messages
            inputbox = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="conversation-compose-box-input"]')
            inputbox.send_keys(value)
            
            #send text message   
            click_element("span[data-icon='send']") 

        except:
            print(key + " can't sent message")
            try:
                click_element("span[data-icon='x-alt']", 10, 30)
                continue
            except:
                sleep(30)
                continue

        #send attachment 1
        # try:
        #     send_attachment('D:/Gilang/Business/Sky/marketing/offering/price_list.jpg')

        # except:
        #     print(key + " cannot send attachment 1")
        #     try:
        #         click_element("span[data-icon='x-alt']", 10, 30)
        #         continue
        #     except:
        #         sleep(30)
        #         continue
            
        # #send attachment 2
        # try:
        #     send_attachment('D:/Gilang/Business/Sky/marketing/offering/offering.pdf')

        # except:
        #     print(key + " cannot send attachment 2")
        #     try:
        #         click_element("span[data-icon='x-alt']", 10, 30)
        #         continue
        #     except:
        #         sleep(30)
        #         continue

        # #send contact
        # try:
        #     send_contact(cp)
        
        # except:
        #     print(key + " cannot send contact details")
        #     try:
        #         click_element("span[data-icon='x-alt']", 10, 30)
        #         continue
        #     except:
        #         sleep(30)
        #         continue

        #success
        print(key + " done")
    

    #delay to next contact
    finally:
        i+=1
        
        if i == 100:
            print("messages sent to 100 contacts. please wait before sending another message.")
            driver.quit()
        
        sleep(30)