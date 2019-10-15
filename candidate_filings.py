from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import csv
import time

def candidateFilings():
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

    url = 'https://secure.sos.state.or.us/orestar/CFSearchPage.do'
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome('/code/chromedriver', chrome_options=options)

    # Go to website
    driver.get(url)
    try:
        myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'cfyearActive')))
        print("Page is loaded!")
    except TimeoutException:
        print("Loading took too much time!")



    # For options in #cfyearActive
    election_year = driver.find_element_by_name('cfyearActive')
    submit = driver.find_element_by_id('submitSearch')
    for option in range(len(election_year.find_elements_by_tag_name('option'))-1):
        if option > 0:
            election_year.find_elements_by_tag_name('option')[option].click()
            # Click Submit
            submit.click()

            try:
                myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'cfSearchResults')))
                print("Results are ready!")
            except TimeoutException:
                print("Loading took too much time!")

            print("Searching")
            results = driver.find_element_by_xpath('//*[@id="cfSearchResults"]/tbody')
            rows = results.find_elements_by_tag_name('tr')
            if len(rows) > 1:
                print('page works')

    
    # if #cfSearchResults has cellClass
        # Add Ballot Name, Party, Office, Election, Filing Method. Filing Date. Qualified
        # Click Link that text matches Ballot Name
            # Add Candidate Filing Source, Election, Office Sought, Residence Address, Filing Type, Work Telephone, Home Telephone
            # ... Work Telephone, Cell, Fax, Email address, Website, occupation, occupational background, educational Background
            # ... educational background (Other), Prior Governmental Experince
        # Click back to search results
    # if next button exist click
    # if next button is disabled create csv and move to next #cfyearActive
candidateFilings()