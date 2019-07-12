from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import csv
import time

def docPull():
    #Pass arguments to the Chrome Driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
    "download.default_directory": './code/download',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('start-maximized')
    options.add_argument('prompt_for_download=False')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.set_headless(headless=True)
    options.binary_location = "/usr/bin/google-chrome-stable"
    print('options collected')

    url = 'https://secure.sos.state.or.us/orestar/gotoPublicTransactionSearch.do'
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome('/code/chromedriver', chrome_options=options)

    #Open chrome and navigate to webpage
    
    driver.get(url)
    print('loading page')

    #print website source code
    # print(driver.page_source)

    #Grab form and button elements
    start = driver.find_element_by_id('cneSearchTranStartDate')
    end = driver.find_element_by_id('cneSearchTranEndDate')
    search_button = driver.find_element_by_name('search')

    #Clear form input by default and input start and end dates
    start.clear()
    start.send_keys('01/01/2012')
    end.clear()
    end.send_keys('01/15/2012')
        
    #click search button
    search_button.click()
    print('searching dates')
    
    try:
        wait = WebDriverWait(driver, 10)
        # download = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Excel Format"))).send_keys(Keys.COMMAND + 't') 
        download = driver.find_element_by_partial_link_text('Excel Format')
        #Download the excel file
        download.click()
        time.sleep(30)
        driver.quit()
        print("downloading file")

    except TimeoutException:
        print("Loading took too much time!")

docPull()