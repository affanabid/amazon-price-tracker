from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import smtplib

# storing the credentials as constants to access gmail accound
MY_EMAIL = "your-gmail-here"
MY_PASSWORD = "your-gmail-password-here"

# setting up the chrome driver to access the desired website and scrape desired data
chrome_driver_path = 'C:/Users/acer/Desktop/udemy-class/Day-48-Selenium/chromdriver.exe'
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url='https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1')
price = int(driver.find_element(By.CLASS_NAME, "a-price-whole").text)

driver.quit()

# comparing the current price with the set price and sending the mail to the user to inform whether 
# the price is in budget now or not
if price < 80:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs='recipient-email-here',
                                msg=f'Subject:Amazon product price declined\n\nThe price of the product you wanted to buy has declined and now lies in your budget range.\nPrice now {price}.')

else:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs='affan.abid99@gmail.com',
                                msg=f'Subject:Still out of your budget\n\nThe price of the product you wanted to buy is still the same.\nPrice now {price}.')
