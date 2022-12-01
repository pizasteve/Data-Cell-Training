from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def call_driver():
    # get the webstie
    link = "https://www.avito.ma"
    driver.get(link)
    # wait for the driver to lead
    time.sleep(1) 

    # find search_bar and search for laptop devices
    search_bar = driver.find_element(By.CLASS_NAME, "sc-1i9i8oo-0")
    search_bar.send_keys("laptop")
    search_bar.send_keys(Keys.ENTER)

    # click on the city filter
    buttons = driver.find_elements(By.CLASS_NAME, "sc-13f8628-0")
    city = buttons[1]
    city.click()

    # click on rabat
    rabat = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/div[1]/span[1]")
    rabat.click()

    recherche = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[3]/button[1]")
    recherche.click()

    # items = driver.find_elements(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div")
    # for item in items:
    #     img = item.find_element(By.XPATH, "/a[1]/div[1]/div[1]/img[1]")
    #     print(img.get_attribute("src")) 

    time.sleep(1)
    pictures = driver.find_elements(By.XPATH, "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[6]/div[1]/div[1]/div[2]/div/a[1]/div[1]/div[1]/img[1]")
    for picture in pictures:
        print(picture.get_attribute("src"))    
    

call_driver()


time.sleep(60)

