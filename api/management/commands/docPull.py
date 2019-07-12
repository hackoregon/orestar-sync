from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from django.core.management.base import BaseCommand
import csv
import time

class Command(BaseCommand):
    help = 'Pulls the documents from search results'

    def handle(self, *args, **kwargs):
        #Open chrome and navigate to webpage
        url = 'https://secure.sos.state.or.us/orestar/gotoPublicTransactionSearch.do'
        print('url collected')
    
        #Pass arguments to the Chrome Driver
        options = Options()
        prefs = {"download.default_directory" : "./code/downloads"}
        options.add_experimental_option("prefs",prefs)
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.set_headless(headless=True)
        options.binary_location = "/usr/bin/google-chrome-stable"
        print('options collected')

        #Initiate Driver
        driver = webdriver.Chrome('/code/chromedriver', chrome_options= options)
        delay = 3

        print('driver created')

        #Go to Orestar Transaction Search page
        driver.get(url)

        #Wait until page is loaded
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'header2')))
            print("submitting search query")
        except TimeoutException:
            print("loading took too much time!")

        #Grab form and button elements
        start = driver.find_element_by_id('cneSearchTranStartDate')
        end = driver.find_element_by_id('cneSearchTranEndDate')
        search_button = driver.find_element_by_name('search')

                #Clear form input by default and input start and end dates
        start.clear()
        start.send_keys(input('Enter your start date: '))
        end.clear()
        end.send_keys(input('Enter your end date: '))

        #click search button
        search_button.click()
        print('searching specified dates')
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "shadedHeader")))
        finally:
            driver.quit()
            driver.get(url)
        print('export available')
            
        dwn_load = driver.find_element_by_partial_link_text('Export')
        dwn_load.click()
        print('downloading file')

