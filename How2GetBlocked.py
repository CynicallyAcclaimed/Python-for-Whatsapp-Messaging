import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name='Victim' #insert the name of the desired recipient/group
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box=driver.find_element_by_xpath("(//div[@class='_2S1VP copyable-text selectable-text' and @data-tab='1'])")

f=open('TextFile.txt','r',encoding="utf8")
for line in f:
    for word in line.split():
        #print(word)
        msg_box.send_keys(word)
        time.sleep(0.5)        
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
