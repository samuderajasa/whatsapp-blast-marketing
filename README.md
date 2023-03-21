# Whatsapp Blast :robot:
Send mass message with whatsapp automation to reach more customer. The code is safe to use as it automate official whatsapp web (not 3rd party software) using [Selenium](https://www.selenium.dev/)

## Requirements :memo:
### 1. Python
Make sure you have Python installed as it written in python language.
- You can [download python here](https://www.python.org/downloads/)
- [How to install python](https://www.digitalocean.com/community/tutorials/install-python-windows-10)
### 2. Pandas
To install pandas library, open command line (Powershell/CMD/terminal):

`pip install pandas`
### 3. Numpy
To install pandas library, open command line:

`pip install numpy`
### 4. Selenium
To install selenium, open command line:

`pip install selenium`

### 5. ChromeDriver
[Download ChromeDriver here](https://chromedriver.chromium.org/downloads) then install it on your computer

## How to Use :book:
### 1. Clone this repository
Download [zip file](https://github.com/samuderajasa/whatsapp-blast-marketing/archive/refs/heads/master.zip) or using Git `git clone https://github.com/samuderajasa/whatsapp-blast-marketing.git`

### 2. First login
This first step will save your session, so you don't have to login every time you run the main code. 
Replace the chromedriver executable path at line 23 to your path where the chromedriver.exe installed.

`ser = Service(r"C://your/folder/path/chromedriver.exe")`

Open command line:

`python auth.py`

It will open the chromedriver and go to whatsapp web. You just need to scan the QR code.

### 3. Prepare your message list
Open the template csv file. The code only reads column A (phone number), column B (contact name) and column C (message).
Quick tips: You can use spreadsheet formula like `=concatenate()` to customize your recipient name

### 4. Start mass messaging
Replace the chromedriver executable path at line 77 to your path where the chromedriver.exe installed.

`ser = Service(r"C://your/folder/path/chromedriver.exe")`

Open command line:

`python main.py`

The code will run in background. You can monitor the message status in the command line:
- .. done -> sent successfully
- .. is not found -> the recipient is not on whatsapp or not in your saved contact list

## Limitation :warning:
+ This code limit 100 messages for safety purpose. You can simply run it again to send more messages. Be careful of getting banned by WA
+ You can't send to recipients that not in saved contact list. (I still trying to figure it out the most efficent way)
