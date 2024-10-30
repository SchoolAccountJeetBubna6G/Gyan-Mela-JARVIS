from selenium import webdriver

from selenium.webdriver.chrome.service import Service

chromedriver = "F:\chromedriver-win64\chromedriver-win64\chromedriver-win64"

option = webdriver.ChromeOptions()

option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

s = Service(chromedriver)

driver = webdriver.Chrome(service=s, options=option)

driver.get("https://google.com")