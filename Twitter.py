from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import random

# Twitter credentials
twitter_username = "Enter Your Username/Email"
twitter_password = "Enter Your Password"
twitter_attherateusername='@Username'

# XLSX File Reading
excel_file_path = pd.read_excel("profile_links.xlsx", header=None, names=['Profile Links'])
profile_links = excel_file_path['Profile Links'].tolist()

# Configuring the Chrome driver and Handling Notification Alert
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

# Log in to Twitter
driver.get("https://twitter.com/i/flow/login")

time.sleep(2)

# Xpath for Username Input
username_input_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'

# Locating Username Input XPath
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, username_input_xpath))
)

# Inputting the Username
username_input.send_keys(twitter_username)

# Clicking on Next Button
next_button_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
next_button = driver.find_element(By.XPATH, next_button_xpath)
next_button.click()

# Wait for 2 seconds for the next page to reload
time.sleep(2)

try:
    # XPath of Phone/Username Field
    phone_input_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
    phone_input = driver.find_element(By.XPATH, phone_input_xpath)

    # Input the phone number or username
    phone_input.send_keys(twitter_attherateusername)  # Replace with your phone number or username

    # Clicking on Next Button
    next_button_phone_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div'
    next_button_phone = driver.find_element(By.XPATH, next_button_phone_xpath)
    next_button_phone.click()

    # Wait for 2 seconds for the next page to reload
    time.sleep(2)

except NoSuchElementException:
    # If the phone number input is not asked, no need to do anything
    print("No phone number asked")

# Wait for 2 seconds for the next page to reload
time.sleep(1)

# XPath for Password Input Field
password_input_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
password_input = driver.find_element(By.XPATH, password_input_xpath)

# Inputting the Password
password_input.send_keys(twitter_password)

# XPath for Submit Button
submit_button_xpath = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'
submit_button = driver.find_element(By.XPATH, submit_button_xpath)

# Clicking on Submit Button
submit_button.click()

# Delay to allow Login Process
time.sleep(5)

#Your Custom Message to be sent to Profile Links
number = 1
text = "your message"

# Limit the number of messages sent in total and within a specific timeframe
max_messages = 50  # Set your desired maximum number of messages
messages_sent = 0
time_interval = 600  # Set the time interval in seconds (e.g., 10 minutes)

# Loop through each row in the Excel sheet
for profile_link in profile_links:
    try:
        if messages_sent >= max_messages:
            print("Stress test limit reached. Exiting...")
            break

        driver.get(profile_link)
        driver.implicitly_wait(10)  # Wait for Website to Load

        # XPath for the message button
        message_button_xpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div'

        message_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, message_button_xpath))
        )
        message_button.click()

        time.sleep(2)
        # XPath for the message input field
        message_input_xpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div/aside/div[2]/div[2]/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]'

        # Wait for the messaging popup to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, message_input_xpath))
        )

        # Find the message input field using XPath
        msg = driver.find_element(By.XPATH, message_input_xpath)

        for letters in text:
            msg.send_keys(letters)
            time.sleep(random.uniform(0.1, 0.3))

        msg.send_keys(Keys.ENTER)
        print("Message sent to\t", profile_links)

        messages_sent += 1

        # Pause the script to avoid rapid actions
        time.sleep(random.uniform(3.2, 4.5))

        # Implement time interval check to prevent continuous messaging within a short timeframe
        if messages_sent % max_messages == 0:
            print(f"Waiting for {time_interval / 60} minutes to avoid detection...")
            time.sleep(time_interval)

    except Exception as e:
        print("Error sending message to", profile_links, ":", e)

    print(number, "-----------------------------------------Msg_automate_kaux---------------------------------------------")
    number += 1

driver.quit()
