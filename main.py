import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

os.environ['PATH'] += ':{}{}webdrivers{}'.format(os.path.realpath(os.getcwd()), os.sep, os.sep)

URL = 'https://airbook.nordwindairlines.ru/websky-test/#/search'

def main():
    driver = webdriver.Chrome()
    driver.get(URL)
    WebDriverWait(driver, 3000).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    styles = driver.find_elements_by_tag_name('style')
    # driver.close()

if __name__ == '__main__':
    main()