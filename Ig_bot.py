from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
USER = "XXXXXX"
PASSWORD = "XXXXX"
URL = "https://www.instagram.com/"
chrome_driver_path = "C:\\Users\\XXXXX\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
driver.maximize_window()
time.sleep(5)
#------------------Login--------------------#
cookie = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
cookie.click()
time.sleep(1)
username = driver.find_element(By.NAME, "username")
username.send_keys(USER)
password = driver.find_element(By.NAME, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(5)
save_info = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
save_info.click()
time.sleep(5)
notifications = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')
notifications.click()
time.sleep(5)

#-----------------Send MSG---------------------#
search = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys("Username")
time.sleep(1)
user_link = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
user_link.click()
time.sleep(1)
private_msg = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
private_msg.click()
time.sleep(1)
msg = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
for _ in range(5):
    msg.send_keys("Your message")
    msg.send_keys(Keys.ENTER)
    time.sleep(1)
