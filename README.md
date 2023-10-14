
# Twitter Automated Messaging Tool

I have created a Twitter Automated Messaging Tool using Python to send a private message to the profile links you provide!


## Installation

To install and run this project,

You can download the zip file or Clone the Project Repository using Git with the below command:
```bash
git clone https://github.com/DhruvAthaide/Twitter-Messaging-Automation.git
```


Once, you have installed the Repository then you can cd into the directory and pip install the requirements needed to run the tool:
```bash
cd Twitter-Messaging-Automation
```

```bash
pip install -r requirements.txt
```

Then, you need to create a XLSX File or Excel File and name it:
```bash
Name: profile_links.xlsx
```

Then, you need to set the following column name in the Excel File and paste the Twitter profile's link you want to message in this column:
```bash
Column 1: Profile Links
```

Then, in the 'Twitter.py' file on Line 12 & 13 Enter your Username/Email ID and Password in between the Quotes for the String:
```bash
twitter_username = "Enter Your Username/Email"
twitter_password = "Enter Your Password"
```

Then, in the 'Twitter.py' file on Line 14 Enter your Twitter @Username in between the Quotes for the String as it is required when logging in multiple times:
```bash
twitter_attherateusername='@Username'
```

Then, customize your message which you want to send to the Twitter profile's on Line 92:
```bash
text = "your message"
```

Then, you can simply run the python file and not touch anything and it will execute the message sending to the Twitter profile's provided in the XLSX or Excel File.

## Authors

- [@Dhruv Athaide](https://github.com/DhruvAthaide)
- [@Himanshu Nimonkar](https://github.com/BoomHimanshu)
- [@Chinmay Maitre](https://github.com/Chinmay-Maitre08)


## Languages & Tools Used:
<p align="left"> 
<a href="https://www.python.org/" target="_blank" rel="noreferrer"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.selenium.dev/" target="_blank" rel="noreferrer"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" alt="selenium" width="40" height="40"/> </a>
</p>