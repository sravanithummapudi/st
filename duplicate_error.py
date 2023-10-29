
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from logindata import USERNAME,PASSWORD



driver = webdriver.Firefox()
time.sleep(3)

driver.get('http://www.github.com')

continue_link = driver.find_element(By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive.header-overlay.home-campaign > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu--logged-out.p-responsive.height-fit.position-lg-relative.d-lg-flex.flex-column.flex-auto.pt-7.pb-4.top-0 > div > div > div.position-relative.mr-lg-3.d-lg-inline-block > a')
continue_link.click()
time.sleep(3)
if driver.find_element(By.NAME, 'login'):
    pass
else:
    time.sleep(2)
    
login = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME, "password")
time.sleep(0.5)
    
login.send_keys(USERNAME)
time.sleep(1)
    
password.send_keys(PASSWORD)
time.sleep(1)
    
button = driver.find_element(By.NAME, 'commit')
button.click()
print ("Here 1")
time.sleep(5)
print ("Here 2")


time.sleep(3)

new_repository = driver.find_element(By.ID, 'global-create-menu-button')
new_repository.click()
time.sleep(1)
new_repository2 = driver.find_element(By.LINK_TEXT, 'New repository')
new_repository2.click()
time.sleep(5)

repository_name = driver.find_element(By.ID, ':r2:')
repository_name.send_keys('github-automation-p9999')
time.sleep(2)

repository_description = driver.find_element(By.ID, ':r3:')
repository_description.send_keys('GitHub Automation Using Selenium Part')
time.sleep(2)

repository_auto_init = driver.find_element(By.ID, ':r8:')
repository_auto_init.click()
time.sleep(2)   

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

create_repo_button = driver.find_element(By.XPATH, '//button[@class="types__StyledButton-sc-ws60qy-0 iqZIXT"]')
create_repo_button.click()
time.sleep(5)

try:
    error1 = driver.find_element(By.CLASS_NAME, 'Box-sc-g0xbh4-0 lbunpI')
    if "already exists" in error1.text:
        print("The repository already exists.")
except NoSuchElementException:
    print("Repository created successfully")
    driver.quit()


print("Here 3")