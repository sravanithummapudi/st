import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
time.sleep(1)

driver.get('http://www.github.com')

repo_link = driver.find_element(By.XPATH, '//summary[@class="btn ml-2"]')
repo_link.click()
time.sleep(4)


upload_button = driver.find_element(By.LINK_TEXT, 'Upload files')
upload_button.click()
time.sleep(3)


print("Here 4")

upload_button2 = driver.find_element(By.XPATH, '//p[@class="repo-file-upload-choose"]')
upload_button2.click()

time.sleep(5)

wsh= comclt.Dispatch("WScript.Shell")

wsh.SendKeys("{TAB}") # send the keys you want
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)

wsh.SendKeys("{DOWN}")
time.sleep(1)
wsh.SendKeys("{DOWN}")
time.sleep(1)   
wsh.SendKeys("{DOWN}")
time.sleep(1)
wsh.SendKeys("{DOWN}")
time.sleep(1)
wsh.SendKeys("{ENTER}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{DOWN}")
time.sleep(1)
wsh.SendKeys("{UP}")
time.sleep(1)
wsh.SendKeys("{ENTER}")

file_name_check="README1.md"
try:
    file_element=driver.find_element(By.LINK_TEXT,file_name_check)
    print(f"File '{file_name_check}' exists in repository and the current file is replacing it")
except NoSuchElementException:
    print(f"File '{file_name_check}' does not exist in repository")

time.sleep(15)

commit_changes = driver.find_element(By.XPATH, '//button[@class="js-blob-submit btn-primary btn"]')
commit_changes.click()
time.sleep(15)