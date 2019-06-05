from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from django.core.management.base import BaseCommand
import csv


# display = 
class Command(BaseCommand):
    help = 'Selenium Based Scrapper for OreStar'

    def handle(self, *args, **kwargs):
        
        #Open chrome and navigate to webpage
        url = 'https://secure.sos.state.or.us/orestar/gotoPublicTransactionSearch.do'
        print('Url Collected')
        
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
        print('options aggrgated')

        #Initiate Driver
        driver = webdriver.Chrome('/code/chromedriver', chrome_options= options)
        delay = 3

        print('driver created')

        #Go to Orestar Transaction Search page
        driver.get(url)

        #print website source code
        # print(driver.page_source)

        #Grab form and button elements
        start = driver.find_element_by_id('cneSearchTranStartDate')
        end = driver.find_element_by_id('cneSearchTranEndDate')
        search_button = driver.find_element_by_name('search')

        #Clear form input by default and input start and end dates
        start.clear()
        start.send_keys('01/01/2016')
        end.clear()
        end.send_keys('02/01/2016')

        #Wait until page is loaded
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'header2')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            
        #click search button
        search_button.click()
        print('Searching specified dates')

        table = driver.find_element_by_xpath('//*[@id="content"]/div/form/table[4]/tbody')
        headings = driver.find_elements_by_xpath('//*[@id="content"]/div/form/table[4]/tbody/tr[1]/td')
        even_rows = driver.find_elements_by_class_name('evenRow')
        odd_rows = driver.find_elements_by_class_name('oddRow')

        transactions = []

        for h in table.find_elements_by_xpath('.//tr'):
            transactions.append([td.text for td in h.find_elements_by_xpath('.//td')])
        myFile = open('csv-write-data.csv', 'w')
        with myFile:
                writer = csv.writer(myFile)
                writer.writerows(transactions)
        
        # for h in headings.find_elements_by_xpath('.//tr'):
        #     transactions.append([td.text for td in h.find_elements_by_xpath('.//td')])
        # print(transactions)

        # print(list(even_rows[0].text))

        # for col in even_rows:

        #     tran_id = 
        #     tran_date = 
        #     status = 
        #     filer = 
        #     payee = 
        #     sub_type = 
        #     amount = 
            
        # for col in odd_rows:
        #     print(col.text)

        
        #Download the excel file
        # download  = driver.find_element_by_link_text('Export To Excel Format').get_attribute('href')
        # print(download)
        # filename = urllib.request.urlretrieve(str(download))
        # open(filename[0])

        # download.click()
        print('file-downloaded')

        # print(start)
        # print(end)
        # print(search_button)

# //TODO: if table is less then 1 then stop the job
# //TODO: click the next button after the file has been written
# //TODO: change the name of the file to [month][day][year][hour][minutes]
# //TODO: Write test coverage plan
# //TODO: Write loading script template for csv files to postgres db
# //TODO: Write chron job to run process once a day