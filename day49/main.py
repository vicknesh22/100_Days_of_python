from selenium import webdriver

driver_path = "/home/vicknesh/Downloads/chromedriver"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://google.com")