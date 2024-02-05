# from selenium import webdriver
# from getpass import getpass
# from webdriver_manager.chrome import ChromeDriverManager 

# username = input('Pl Enter Your Facebook username: ')
# passwd = getpass('Enter your Facebook password: ')

# #driver = webdriver.Chrome(ChromeDriverManager().install)
# driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver')
# driver.get('https://meroshare.cdsc.com.np/#/login')

# select_dp = driver.find_element_by_id('select2-sh77-container')
# select_dp.send_keys(username)

# txtusername = driver.find_element_by_id('username')
# txtusername.send_keys(passwd)

# txtPasswd = driver.find_element_by_id('password')
# txtPasswd.send_keys(passwd)

# btnLogin = driver.find_element_by_id('u_0_b')
# btnLogin.submit()
import time
from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui





# Using ChromeDriverManager to automatically download the appropriate chromedriver
chrome_driver_path = ChromeDriverManager().install()

# Create ChromeOptions instance
chrome_options = webdriver.ChromeOptions()

# Use the downloaded chromedriver and add it to the ChromeOptions
chrome_options.add_argument(f"webdriver.chrome.driver= C:/chromedriver")




# Initialize the webdriver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Replace the URL with the correct login page URL
driver.get('https://meroshare.cdsc.com.np/#/login')

time.sleep(2)
dp = '11000'
username = '307727'
passwd = 'Iwtb93@MS'

#driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
# select_dp = driver.find_element(By.CLASS_NAME, 'app header-fixed sidebar-fixed aside-menu-fixed aside-menu-hidden')
# select_dp.click()
# select_dp.send_keys(Keys.TAB)
# select_dp.send_keys(Keys.ENTER)
time.sleep(2)

pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.typewrite('11000')
pyautogui.press('enter')

time.sleep(2)
 # Use appropriate element locators for the website
#select_dp = driver.find_element_by_id('select2-vvac-container')
#'select_dp = driver.find_element(By.ID, 'select2-vvac-container')
#select_dp.send_keys(dp)


# Find the element by ID

# element_by_id = driver.find_element(By.ID, 'select2-9361-container')
# # Click on the element
# element_by_id.click()

# time.sleep(2)






txtusername = driver.find_element(By.ID, 'username')
#txtusername = driver.find_element_by_id('username')
txtusername.send_keys(username)
time.sleep(2)

txtPasswd = driver.find_element(By.ID, 'password')
#txtPasswd = driver.find_element_by_id('password')
txtPasswd.send_keys(passwd)

txtPasswd.send_keys(Keys.ENTER)

time.sleep(5)

# btnLogin = driver.find_element(By.CLASS_NAME, 'btn sign-in')
# #btnLogin = driver.find_element_by_id('u_0_b')
# btnLogin.Enter()


#WebElement.sendKeys(Keys.RETURN)
