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
    help = 'Selenium Based Scrapper for OreStar'

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
        start.send_keys('06/15/2019')
        end.clear()
        end.send_keys('06/20/2019')
            
        #click search button
        search_button.click()
        print('searching specified dates')
        
        table = driver.find_element_by_tag_name('tr')
        next_btn = driver.find_element_by_name('next')

        transactions = []


        #while the number of rows is greater than 1 find and click the next button to repeat the following steps
        while len(driver.find_elements_by_class_name('evenRow')) > 1:
            table = driver.find_element_by_tag_name('tr')
            even_rows = table.find_elements_by_class_name('evenRow')
            odd_rows = table.find_elements_by_class_name('oddRow')
            rows = even_rows + odd_rows

            #insert items into a list
            for items in rows:
                individual = []
                odd_chars = ['$', '"']
                #insert individual transactions into a list
                for cell in items.find_elements_by_xpath('.//td'):
                    if odd_chars in cell:
                        individual.append(cell.text)
                transactions.append(individual)

            try:
                wait_for_next = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "next"))
                )
            finally:
                next_btn = driver.find_element_by_name('next')
                next_btn.click()
                print('next page')
        
        else:
            # header = driver.find_element_by_class_name('shadedHeader')
            filename = time.strftime('%Y%m%d-%H%M%S')
            myFile = open('{}.csv'.format(filename), 'w')
            with myFile:
                writer = csv.writer(myFile)
                writer.writerow([
                    'Trans ID', 
                    'Original ID', 
                    'Trans Date', 
                    'Filer', 
                    'Payee', 
                    'SubType', 
                    'Amount',
                    'Agg Amount',
                    'Payee ID',
                    'Filer ID',
                    'Attest by Name',
                    'Attest Date',
                    'Review by name',
                    'Review Date',
                    'Due Date',
                    'Occptn ltr date',
                    'Payment Text',
                    'Purps Desc',
                    'Interest',
                    'check_numb',
                    'trans_status_ind',
                    'File by Name',
                    'File Date',
                    'Address Book Agent',
                    'Book Type',
                    'Title Text',
                    'Occptn TXT',
                    'emp_name',
                    'emp_city',
                    'emp state',
                    'employeed',
                    'self employeed',
                    'Address line 1',
                    'Address line 2',
                    'city',
                    'state',
                    'zipcode',
                    'zipplus',
                    'county',
                    'purpose code'
                    ])
                writer.writerows(
                    transactions
            )

        print('Records downloaded to {}.csv'.format(filename))

# //TODO: Write test coverage plan
# //TODO: Rewrite scraper to download, rename and move the excel file
#// TODO: Rewrite the loading script to match new fields and load from csv file
#// TODO: Write script to download excel files a week at a time