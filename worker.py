from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# display = 

#Open chrome and navigate to webpage
url = 'https://secure.sos.state.or.us/orestar/gotoPublicTransactionSearch.do'
driver = webdriver.Chrome()
delay = 3
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

try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
    
#click search button
search_button.click()

#Download the excel file
download  = driver.find_element_by_link_text('Export To Excel Format')
download.click()

import os
import shutil

filename = max([f for f in os.listdir('c:\downloads')], key=os.path.getctime)
shutil.move(os.path.join(dirpath,filename),newfilename)

# print(start)
# print(end)
# print(search_button)

