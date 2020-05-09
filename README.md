# Python for Whatsapp Messaging - One Word at a Time!
Using Python with Selenium to send messages one word at a time from a text file (aka How to Get Blocked).

#### If you ever wanted to send someone the entire script of the Bee Movie on Whatsapp, this is the code for you. 


### Step 1: You'll need Selenium for this, so go ahead and get that.
```
pip install selenium 
```

### Step 2: Webdriver
You'll need a webdriver to interact with the browser. I'm using Chrome, so I've used chromedriver.
```
from selenium import webdriver
driver = webdriver.Chrome()
```
You can get it from the official site, unzip the folder, and add the .exe file to your working environment. 
(I'm using Jupyter, so it's as simple as just uploading the file)

https://chromedriver.chromium.org/downloads


### Step 3: Log in to Whatsapp
```
driver.get('https://web.whatsapp.com/')
```
This opens Whatsapp Web in a new window, scan the QR code and hop in. 

### Step 4: Code and stuff
```
name='<victim>'
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
```
Insert the name of the person/group you want to spam within the quotes.
This works by interacting with web elements; go ahead and Ctrl+Shift+I if you want to check it out for yourself.

###### Note: The person needs to be relatively high up in your messaging list.

```
msg_box=driver.find_element_by_xpath("(//div[@class='_2S1VP copyable-text selectable-text' and @data-tab='1'])")
```
There are two elements with '_2S1VP' as the class name: the text box, as well as the search bar where you search for contacts. 
Obviously, you want the former, and I've simply done that by including a tag that differentiates the two. 

```
f=open('beemovie.txt','r',encoding="utf8")
for line in f:
    for word in line.split():
        print(word)
        msg_box.send_keys(word)
        time.sleep(0.5)        
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
```
Open the file in Read mode. I've added a delay of 0.5 seconds because any faster, and messages start lagging, and they get sent out of order.
I've found the button by the class name instead of using xpath because it has a unique name.

###### The Send button appears only when there is a message typed in the box (you might have noticed that before that, it's the microphone)

### Step 5: Get blocked!
###### p.s: it helps if you have another means of contacting the person you decide to spam. 
