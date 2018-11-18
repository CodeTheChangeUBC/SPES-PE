import time
import getpass
from selenium import webdriver
class TimeoutException(Exception): pass
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
username = "ctcstanley1@gmail.com"
password = "codethechange"


def eventful(title,date,startTime,endTime,repeats,venue,description,facebookURL):
        driver.get('http://eventful.com/signin?goto=%2Fevents%2Fnew')
        try: 
                usernameField = driver.find_element_by_id("inp-username")
        except NoSuchElementException:
                print('Username field ID changed')
                
        usernameField.send_keys(username)

        try:
                passwordField = driver.find_element_by_id("inp-password")
        except NoSuchElementException:
               print('Password field ID changed')
               
        passwordField.send_keys(password)
        passwordField.submit()

        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'inp-title')))
        except TimeoutException:
            print ("Loading took too much time!")

            
        titleField = driver.find_element_by_id("inp-title")
        titleField.clear()
        titleField.send_keys(title)


        dateField = driver.find_element_by_id("inp-start_date")
        dateField.clear()
        dateField.send_keys(date)

        startTimeField = driver.find_element_by_id("inp-start_time")
        startTimeField.clear()
        startTimeField.send_keys(startTime)

        endTimeField = driver.find_element_by_id("inp-stop_time")
        endTimeField.clear()
        endTimeField.send_keys(endTime)


        repeatsField = Select(driver.find_element_by_id("inp-repeats"))
        repeatsField.select_by_visible_text("-- does not repeat --")

        venueField = driver.find_element_by_id("inp-venue")
        venueField.clear()
        venueField.send_keys(venue)

##      categoryField = Select(driver.find_element_by_name("category1"))
##      categoryField.select_by_visible_text("Film")

        descriptionField = driver.find_element_by_id("inp-description")
        descriptionField.clear()
        descriptionField.send_keys(description)

        facebookEventField = driver.find_element_by_id("inp-fb-event-link")
        facebookEventField.clear()
        facebookEventField.send_keys(facebookURL)

def youthCore(startTime,endTime,title,ageGroup,cost,venue,details,facebookURL):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
        driver.get('http://youthcore.ca/index.php?action=create_event')
        try: 
                nameField = driver.find_element_by_id("submitter_name")
        except NoSuchElementException:
                print('Name field ID changed')
                
        nameField.send_keys(username)

        try:
                emailField = driver.find_element_by_id("submitter_email")
        except NoSuchElementException:
               print('Email field ID changed')
               
        emailField.send_keys(password)

        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'program_name')))
        except TimeoutException:
            print ("Loading took too much time!")

##      dateField = driver.find_element_by_id("datestring")
##      date= "03/05/2018"
##      dateField.send_keys(date)

        startTimeField = driver.find_element_by_id("start_time")
        startTimeField.send_keys(startTime)

        endTimeField = driver.find_element_by_id("end_time")
        endTimeField.send_keys(endTime)

        titleField = driver.find_element_by_id("program_name")
        titleField.send_keys(title)

        ageField = driver.find_element_by_id("age_group")
        ageField.send_keys(ageGroup)

        costField = driver.find_element_by_id("cost")
        costField.send_keys(cost)

        venueField = driver.find_element_by_id("venue_name")
        venueField.send_keys(venue)

        detailsField = driver.find_element_by_id("ta_description")
        detailsField.send_keys(details)

        facebookField = driver.find_element_by_id("ta_facebook_event_url")
        facebookField.send_keys(facebookURL)

def planetFriendly(title,city,province,description,contactName,contactEmail,contactWeb,password):
        driver.get('http://planetfriendly.net/submit3.html')
        
        titleField = driver.find_element_by_name("Title")
        titleField.send_keys(title)

        cityField = driver.find_element_by_name("City")
        cityField.send_keys(city)

        provinceField = Select(driver.find_element_by_name("Province"))
        provinceField.select_by_visible_text("British Columbia")

        descriptionField = driver.find_element_by_name("Descrip")
        descriptionField.send_keys(description)

        contactNameField = driver.find_element_by_name("ContactName")
        contactNameField.send_keys(contactName)

        contactEmailField = driver.find_element_by_name("ContactEmail")
        contactEmailField.send_keys(contactEmail)

        contactPhoneField = driver.find_element_by_name("ContactPhone")
        contactPhoneField.send_keys(contactPhone)

        contactWebField = driver.find_element_by_name("ContactWeb")
        contactWebField.send_keys(contactWeb)

        passwordField = driver.find_element_by_name("Password1")
        password2Field = driver.find_element_by_name("Password2")
        passwordField.send_keys(password)
        password2Field.send_keys(password)

        #Ignore this block of code
        spamField = driver.find_element_by_name("Spam")
        spam = "hello"
        spamField.send_keys(spam)


def globalNews(title,description,venue,street,city,province,description,country,organizerName,organizerEmail,organizerPhone):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
        driver.get('https://globalnews.ca/bc/events/add/')
        nameField = driver.find_element_by_id("event-name")
        nameField.send_keys(title)

        descriptionField = driver.find_element_by_id("event-description")
        descriptionField.send_keys(description)

##      typeField = Select(driver.find_element_by_name("event-type"))
##      typeField.select_by_visible_text("Food")

        venueField = driver.find_element_by_id("event-venue")
        venueField.send_keys(venue)

        streetField = driver.find_element_by_id("event-street")
        streetField.send_keys(street)

        cityField = driver.find_element_by_id("event-city")
        cityField.send_keys(city)

        provinceField = driver.find_element_by_id("event-province")
        provinceField.send_keys(province)

        descriptionField = driver.find_element_by_id("event-description")
        descriptionField.send_keys(description)

        countryField = driver.find_element_by_id("event-country")
        countryField.send_keys(country)

        organizerNameField = driver.find_element_by_id("event-organizer-name")
        organizerNameField.send_keys(organizerName)

        organizerEmailField = driver.find_element_by_id("event-organizer-email")
        organizerEmailField.send_keys(organizerEmail)

        organizerPhoneField = driver.find_element_by_id("event-organizer-phone")
        organizerPhoneField.send_keys(organizerPhone)

def kijiji(price,dateFrom,dateTo,title,description,postalCode,street,organizerPhone):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
        driver.get('https://www.kijiji.ca/t-login.html?targetUrl=L3Atc2VsZWN0LWNhdGVnb3J5Lmh0bWw/Y2F0ZWdvcnlJZD0yODkmdXNlclJlZ2lzdGVyZWQ9dHJ1ZV54Tk1KeU9ySTA5U0Z3MDdzS213OC93PT0-')
        try: 
                usernameField = driver.find_element_by_id("LoginEmailOrNickname")
        except NoSuchElementException:
                print('Username field ID changed')
                
        usernameField.send_keys(username)

        try:
                passwordField = driver.find_element_by_id("login-password")
        except NoSuchElementException:
               print('Password field ID changed')

        passwordField.send_keys(password)
        passwordField.submit()

        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'FormLocationPicker')))
        except TimeoutException:
            print ("Loading took too much time!")

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "British Columbia")))
        element.click()
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Greater Vancouver Area")))
        element.click()
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Vancouver")))
        element.click()

        form = driver.find_element_by_id("PageSelect")
        form.click()
        
        priceField = driver.find_element_by_id("PriceAmount")
        priceField.send_keys(price)

        dateField = driver.find_element_by_id("SelectDate")
        dateField.send_keys(dateFrom)
        
        
        dateToField = driver.find_element_by_id("SelectDateTo")
        dateToField.send_keys(dateTo)

        titleField = driver.find_element_by_id("postad-title")
        titleField.send_keys(title)

        descriptionField = driver.find_element_by_id("pstad-descrptn")
        descriptionField.send_keys(description)

        postalCodeField = driver.find_element_by_id("PostalCode")
        postalCodeField.send_keys(postalCode)

        streetField = driver.find_element_by_id("pstad-map-address")
        streetField.send_keys(street)

        numberField = driver.find_element_by_id("PhoneNumber")
        numberField.send_keys(organizerPhone)


        
def main():
        global driver
        global username
        global password



if __name__ == "__main__":
    main()
