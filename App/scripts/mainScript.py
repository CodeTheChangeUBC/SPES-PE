import time
import json
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
username = "*******@gmail.com"
password = "*******"
websites ={'successful':[],
           'captcha':[],
           'unsuccessful':[]
          }

def eventful(title,date,startTime,endTime,venue,description,facebookURL):
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

##        categoryField = Select(driver.find_element_by_name("category1"))
##        categoryField.select_by_visible_text("Film")

        descriptionField = driver.find_element_by_id("inp-description")
        descriptionField.clear()
        descriptionField.send_keys(description)

        facebookEventField = driver.find_element_by_id("inp-fb-event-link")
        facebookEventField.clear()
        facebookEventField.send_keys(facebookURL)

        websites['captcha'].append("Eventful")
        

def youthCore(startTime,endTime,title,ageGroup,cost,venue,details,facebookURL):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
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

        websites['captcha'].append("Youth Core")


def planetFriendly(title,city,province,description,contactName,contactEmail,contactPhone,contactWeb,password):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
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


def globalNews(title,description,venue,street,city,province,country,organizerName,organizerEmail,organizerPhone):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
        driver.get('https://globalnews.ca/bc/events/add/')
        nameField = driver.find_element_by_id("event-name")
        nameField.send_keys(title)

        descriptionField = driver.find_element_by_id("event-description")
        descriptionField.send_keys(description)

        typeField = Select(driver.find_element_by_name("event-type"))
        typeField.select_by_visible_text("Other")

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
        ## driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
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

def metroVancouver(title,description,location,address,municapility,startDate,endDate,firstName,lastName,phone,email):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
        driver.get('http://www.metrovancouver.org/events/Pages/add-event.aspx')

        titleField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_TitleField_ctl00_ctl00_TextField")
        titleField.send_keys(title)

        descriptionField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_CommentsField_ctl00_ctl00_TextField")
        descriptionField.send_keys(description)

        locationField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_LocationField_ctl00_ctl00_TextField")
        locationField.send_keys(location)

        addressField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_WorkAddressField_ctl00_ctl00_TextField")
        addressField.send_keys(address)

        municapility = Select(driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_MunicipalityDropDownField_ctl00_DropDownChoice"))
        municapility.select_by_visible_text("British Columbia")

        startDateField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_StartDateField_ctl00_ctl00_DateTimeField_DateTimeFieldDate")
        startDateField.send_keys(startDate)

        endDateField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_StartDateField_ctl00_ctl00_DateTimeField_DateTimeFieldDate")
        endDateField.send_keys(endDate)
        
        firstNameField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_FirstNameField_ctl00_ctl00_TextField")
        firstNameField.send_keys(firstName)

        lastNameField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_LastNameField_ctl00_ctl00_TextField")
        lastNameField.send_keys(lastName)

        phoneField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_PhoneField_ctl00_ctl00_TextField")
        phoneFiled.send_keys(phone)

        emailField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_EMailField_ctl00_ctl00_TextField")
        emailField.send_keys(email)

        websites['captcha'].append("Metro Vancouver")

        

def cnv(submitterName,email,title,location,organizer,name,phone,url):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
        browser.get('http://www.cnv.org/Parks-Recreation-and-Culture/Community-Events/Submit-an-Event')


        browser.implicitly_wait(10)
        browser.switch_to.frame("trumbaSubmitEventForm")

            
        submitterNameField = browser.find_element_by_id("eaa_TextboxName")
        submitterNameField.clear()
        submitterNameField.send_keys(submitterName)

        emailField = browser.find_element_by_id("eaa_TextboxEmail")
        emailField.clear()
        emailField.send_keys(email)

        titleField = browser.find_element_by_id("eaa_custom3_0")
        titleField.clear()
        titleField.send_keys(title)

        locationField = browser.find_element_by_id("eaa_TextboxLocation")
        locationField.clear()
        locationField.send_keys(location)

        startMonthField = Select(browser.find_element_by_id("eaa_DropDownStartMonth"))
        startMonthField.select_by_visible_text("May")
        startMonthField = Select(browser.find_element_by_id("eaa_DropDownStartDay"))
        startMonthField.select_by_visible_text("2")
        startMonthField = Select(browser.find_element_by_id("eaa_DropDownStartYear"))
        startMonthField.select_by_visible_text("2017")

        startTimeHrField = Select(browser.find_element_by_id("eaa_DropDownStartHour"))
        startTimeHrField.select_by_visible_text("11")
        startTimeMinField = Select(browser.find_element_by_id("eaa_DropDownStartMinute"))
        startTimeMinField.select_by_visible_text("20")
        startTimeField = Select(browser.find_element_by_id("eaa_DropDownStartAMPM"))
        startTimeField.select_by_visible_text("PM")

        endTimeHrField = Select(browser.find_element_by_id("eaa_DropDownEndHour"))
        endTimeHrField.select_by_visible_text("11")
        endTimeMinField = Select(browser.find_element_by_id("eaa_DropDownEndMinute"))
        endTimeMinField.select_by_visible_text("40")
        endTimeField = Select(browser.find_element_by_id("eaa_DropDownEndAMPM"))
        endTimeField.select_by_visible_text("PM")

        organizerField = browser.find_element_by_id("eaa_custom29378_0")
        organizerField.clear()
        organizerField.send_keys(organizer)

        nameField = browser.find_element_by_id("eaa_custom29379_0")
        nameField.clear()
        nameField.send_keys(name)

        phoneField = browser.find_element_by_id("eaa_custom29380_0")
        phoneField.clear()
        phoneField.send_keys(phone)

        emailField = browser.find_element_by_id("eaa_custom29641_0")
        emailField.clear()
        emailField.send_keys(email)

        urlField = browser.find_element_by_id("eaa_custom6_0")
        urlField.clear()
        urlField.send_keys(url)

def ubyssey(title,description,host,startTime,endTime,location,address,ticket,email,phone):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
        browser.get('https://www.ubyssey.ca/events/submit/form')
        
        try:
            myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'id_title')))
        except TimeoutException:
            print("Loading took too much time!")
            browser.quit()
            
        titleField = browser.find_element_by_id("id_title")
        titleField.clear()
        titleField.send_keys(title)

        descriptionField = browser.find_element_by_id("id_description")
        descriptionField.clear()
        descriptionField.send_keys(description)

        hostField = browser.find_element_by_id("id_host")
        hostField.clear()
        hostField.send_keys(host)

        categoryField = Select(browser.find_element_by_id("id_category"))
        categoryField.select_by_visible_text("Academic")

        startTimeField = browser.find_element_by_id("id_start_time")
        startTimeField.clear()
        startTimeField.send_keys(startTime)

        endTimeField = browser.find_element_by_id("id_end_time")
        endTimeField.clear()
        endTimeField.send_keys(endTime)

        locationField = browser.find_element_by_id("id_location")
        locationField.clear()
        locationField.send_keys(location)

        addressField = browser.find_element_by_id("id_address")
        addressField.clear()
        addressField.send_keys(address)

        ticketField = browser.find_element_by_id("id_ticket_url")
        ticketField.clear()
        ticketField.send_keys(ticket)

        emailField = browser.find_element_by_id("id_submitter_email")
        emailField.clear()
        emailField.send_keys(email)

        phoneField = browser.find_element_by_id("id_submitter_phone")
        phoneField.clear()
        phoneField.send_keys(phone)

def northShore(name,email,phone,title,description,webLink):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
        browser.get('http://www.nsnews.com/add-event')
        browser.switch_to.frame("trumbaSubmitEventForm");

        try:
            myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'eaa_TextboxName')))
        except TimeoutException:
            print("Loading took too much time!")
            browser.quit()

        nameField = browser.find_element_by_id("eaa_TextboxName")
        nameField.clear()
        nameField.send_keys(name)

        emailField = browser.find_element_by_id("eaa_TextboxEmail")
        emailField.clear()
        emailField.send_keys(email)

        phoneField = browser.find_element_by_id("eaa_TextboxPhone")
        phoneField.clear()
        phoneField.send_keys(phone)

        titleField = browser.find_element_by_id("eaa_custom3_0")
        titleField.clear()
        titleField.send_keys(title)


        descriptionField = browser.find_element_by_id("eaa_TextboxLocation")
        descriptionField.clear()
        descriptionField.send_keys(description)

        startDayField = Select(browser.find_element_by_id("eaa_DropDownStartMonth"))
        startDayField.select_by_visible_text("May")
        startMonthField = Select(browser.find_element_by_id("eaa_DropDownStartDay"))
        startMonthField.select_by_visible_text("2")
        startMonthField = Select(browser.find_element_by_id("eaa_DropDownStartYear"))
        startMonthField.select_by_visible_text("2018")

        startTimeHrField = Select(browser.find_element_by_id("eaa_DropDownStartHour"))
        startTimeHrField.select_by_visible_text("11")
        startTimeMinField = Select(browser.find_element_by_id("eaa_DropDownStartMinute"))
        startTimeMinField.select_by_visible_text("20")
        startTimeField = Select(browser.find_element_by_id("eaa_DropDownStartAMPM"))
        startTimeField.select_by_visible_text("PM")

        durationField = Select(browser.find_element_by_id("eaa_DropDownDurationHours"))
        durationField.select_by_visible_text("3 hours")

        eventTypeField = Select(browser.find_element_by_id("eaa_custom17792_0_selectedItems"))
        eventTypeField.select_by_visible_text("All ages")

        webLinkField = browser.find_element_by_id("eaa_custom6_0")
        webLinkField.clear()
        webLinkField.send_keys(webLink)

        descriptionField = browser.find_element_by_id("eaa_custom4_0")
        descriptionField.clear()
        descriptionField.send_keys(description)

def craigsList(title,postalCode,description,email,phone,street,city):
        ## driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
        browser.get('http://post.craigslist.org/k/6LCtjvRV6BGHSA6-sDz7FA/5ViVw?lang=en&cc=us&s=edit')
        try:
            myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'PostingTitle')))
        except TimeoutException:
            print("Loading took too much time!")
            browser.quit()

        titleField = browser.find_element_by_id("PostingTitle")
        titleField.clear()
        titleField.send_keys(title)

        postalCodeField = browser.find_element_by_id("postal_code")
        postalCodeField.clear()
        postalCodeField.send_keys(postalCode)

        descriptionField = browser.find_element_by_id("PostingBody")
        descriptionField.clear()
        descriptionField.send_keys(description)

        durationField = Select(browser.find_element_by_name("eventDuration"))
        durationField.select_by_index(0)

        emailField = browser.find_element_by_id("FromEMail")
        emailField.clear()
        emailField.send_keys(email)

        emailField = browser.find_element_by_id("ConfirmEMail")
        emailField.clear()
        emailField.send_keys(email)

        phoneField = browser.find_element_by_id("contact_phone")
        phoneField.clear()
        phoneField.send_keys(phone)

        streetField = browser.find_element_by_id('xstreet0')
        streetField.clear()
        streetField.send_keys(street)

        cityField = browser.find_element_by_id('city')
        cityField.clear()
        cityField.send_keys(city)




def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

        
        
def main():
        global driver
        global username
        global password

        f = open('C:/Users/Nadeem AbdelAziz/Desktop/Extracurriculars/sample.json', "r")
        s = f.read()
        info = json.loads(s)


        writeToJSONFile("./", "sample", websites)

        print(websites)


if __name__ == "__main__":
    main()
