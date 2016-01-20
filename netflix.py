from selenium import webdriver

print('Input your email')
userEmail = input()
print('Input password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('https://login.microsoftonline.com/')


loginElem = browser.find_element_by_id('cred_userid_inputtext')
loginElem.click ()

#emailElem = browser.find_element_by_id('cred_userid_inputtext')
#emailElem.send_keys (userEmail)
loginElem.send_keys (userEmail)

passwordElem = browser.find_element_by_id('cred_password_inputtext')
passwordElem.send_keys (userPassword)
passwordElem.submit ()