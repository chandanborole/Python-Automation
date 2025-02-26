from selenium import webdriver

driver=webdriver.Chrome

# Authentication popup code - syntax with example
# Syntax - http://username:password@url
# Example - http://admin:admin@the-internet.herokuapp.com/basic_auth

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
