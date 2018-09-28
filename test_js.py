from selenium import webdriver


browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "http://example.com/login.php"
browser.get(url) #navigate to the page