import time
import json
import sys
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
websites ={'successful':[],
           'captcha':[],
           'unsuccessful':[]
          }



def eventful(info):
        title = info['event_title']
        date = info['event_date_start'][:10]
        startTime=info['event_date_start'][12:]
        endTime = info['event_date_end'][12:]
        venue=info['event_venue']
        description = info['event_details']
        facebookURL = 'test'
        price = info['event_price']
        link = 'tes'
        
        driver.get('http://eventful.com/signin?goto=%2Fevents%2Fnew')
        try: 
                usernameField = driver.find_element_by_id("inp-username")
                usernameField.send_keys(username)
                passwordField = driver.find_element_by_id("inp-password")
                passwordField.send_keys(password)
                passwordField.submit()
        except:
                print("Login form id changed!")

        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'inp-title')))
        except TimeoutException:
            print ("Loading took too much time!")

        try:    
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

           descriptionField = driver.find_element_by_id("inp-description")
           descriptionField.clear()
           descriptionField.send_keys(description)

           
           clickField = driver.find_element_by_id("click-more-options")
           clickField.click()
           priceField = driver.find_element_by_id("inp-price")
           priceField.clear()
           priceField.send_keys(price)

           linkClick = driver.find_element_by_id("event-add-link-click")
           linkClick.click()
           linkField = driver.find_element_by_id("url-add-link")
           linkField.send_keys(link)
           linkClick = driver.find_element_by_id("inp-submit-add-link")
           linkClick.click()

           facebookEventField = driver.find_element_by_id("inp-fb-event-link")
           facebookEventField.clear()
           facebookEventField.send_keys(facebookURL)
        except:
            websites['unsuccessful'].append("Eventful")
        else:
            websites['captcha'].append("Eventful")
        

def youthCore(info):
        driver.execute_script("window.open('http://youthcore.ca/index.php?action=create_event', 'new window')")
        title = info['event_title']
        startTime=info['event_date_start'][12:]
        endTime = info['event_date_end'][12:]
        venue=info['event_venue']
        details = info['event_details']
        facebookURL = info['event_fbURL']
        cost = info['event_price']
        ageGroup = info['event_age_group']
        
        try: 
                nameField = driver.find_element_by_id("submitter_name")
                nameField.send_keys(username)
                emailField = driver.find_element_by_id("submitter_email")
                emailField.send_keys(password)
        except TimeOutException:
               print('Login form id chnaged!')
               

        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'program_name')))
        except TimeoutException:
            print ("Loading took too much time!")
        try:
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
        except:
                websites['unsuccessful'].append("Youth Core")
        else:
                websites['captcha'].append("Youth Core")


def planetFriendly(info):
        driver.execute_script("window.open('http://planetfriendly.net/submit3.html', 'new window')")

        title = info['event_title']
        description = info['event_details']
        city = info['event_city']
        contactName = info['event_organizer_name']
        contactEmail = info['event_organizer_email']
        contactPhone = info['event_organizer_phone_number']
        contactWeb = info['event_url']
        
        try:
                titleField = driver.find_element_by_name("Title")
                titleField.send_keys(title)

##                startDateField = Select(driver.find_element_by_name("StartDate"))
##                startDateField.select_by_visible_text(startDate)
##
##                startMonthField = Select(driver.find_element_by_name("StartMonth"))
##                startMonthField.select_by_visible_text(startMonth)
##
##                startYearField = Select(driver.find_element_by_name("StartYear"))
##                startYearField.select_by_visible_text(startYear)
##
##                endDateField = Select(driver.find_element_by_name("EndDate"))
##                endDateField.select_by_visible_text(endDate)
##
##                endMonthField = Select(driver.find_element_by_name("EndMonth"))
##                endMonthField.select_by_visible_text(endMonth)
##
##                endYearField = Select(driver.find_element_by_name("EndYear"))
##                endYearField.select_by_visible_text(endYear)

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
        except:
                websites['unsuccessful'].append("Planet Friendly")
        else:
                try:
                        driver.implicitly_wait(10)
                        driver.find_element_by_name("ContactName")
                        websites['unsuccessful'].append("Planet Friendly")
                except NoSuchElementException:
                        websites['successful'].append("Planet Friendly")


def globalNews(info):        
        title = info['event_title']
        venue=info['event_venue']
        description = info['event_details']
        age = info['event_age_group']
        city = info['event_city']
        street = info['event_street']
        organizerName = info['event_organizer_name']
        organizerEmail = info['event_organizer_email']
        organizerPhone = info['event_organizer_phone_number']
        eventURL = info['event_url']
        postalCode = info['event_postal_code']
        ticketURL = info['event_ticketURL']


        driver.execute_script("window.open('https://globalnews.ca/bc/events/add/', 'new window')")
        try:
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
                provinceField.send_keys("British Columbia")

                countryField = driver.find_element_by_id("event-country")
                countryField.send_keys("Canada")

                organizerNameField = driver.find_element_by_id("event-organizer-name")
                organizerNameField.send_keys(organizerName)

                organizerEmailField = driver.find_element_by_id("event-organizer-email")
                organizerEmailField.send_keys(organizerEmail)

                organizerPhoneField = driver.find_element_by_id("event-organizer-phone")
                organizerPhoneField.send_keys(organizerPhone)

                agesField = driver.find_element_by_id("event-ages")
                agesField.send_keys(age)

                websiteField = driver.find_element_by_id("event-website")
                websiteField.send_keys(eventURL)
        
                ticketField = driver.find_element_by_id("event-tickets")
                ticketField.send_keys(ticketURL)

                postalCodeField = driver.find_element_by_id("event-postal-code")
                postalCodeField.send_keys(postalCode)

        except:
                websites['unsuccessful'].append("Global News")
        else:
                try:
                        driver.implicitly_wait(10)
                        driver.find_element_by_id("event-organizer-name")
                        websites['unsuccessful'].append("Global News")
                except NoSuchElementException:
                        websites['successful'].append("Planet Friendly")


def kijiji(price,dateFrom,dateTo,title,description,postalCode,street,organizerPhone):
        driver.execute_script("window.open('https://www.kijiji.ca/t-login.html?targetUrl=L3Atc2VsZWN0LWNhdGVnb3J5Lmh0bWw/Y2F0ZWdvcnlJZD0yODkmdXNlclJlZ2lzdGVyZWQ9dHJ1ZV54Tk1KeU9ySTA5U0Z3MDdzS213OC93PT0-'
                              , 'new window')")
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
        try: 
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
        except:
                websites['unsuccessful'].append("Kijiji")
        else:
                try:
                        driver.implicitly_wait(10)
                        driver.find_element_by_id("SelectDate")
                        websites['unsuccessful'].append("Kijiji")
                except NoSuchElementException:
                        websites['successful'].append("Kijiji")


def metroVancouver(info):

        title = info['event_title']
        location=info['event_venue']
        description = info['event_details']
        address = info['event_street']
        organizerName = info['event_organizer_name']
        organizerEmail = info['event_organizer_email']
        organizerPhone = info['event_organizer_phone_number']
        
        driver.execute_script("window.open('http://www.metrovancouver.org/events/Pages/add-event.aspx', 'new window')")
        try:
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
                firstNameField.send_keys(organizerName)

                lastNameField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_LastNameField_ctl00_ctl00_TextField")
                lastNameField.send_keys(organizerName)

                phoneField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_PhoneField_ctl00_ctl00_TextField")
                phoneFiled.send_keys(phone)

                emailField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_EMailField_ctl00_ctl00_TextField")
                emailField.send_keys(email)
        except:
         websites['unsuccessful'].append("Metro Vancouver")
        else:
         websites['captcha'].append("Metro Vancouver")

        

def cnv(info):
        driver.execute_script("window.open('http://www.cnv.org/Parks-Recreation-and-Culture/Community-Events/Submit-an-Event', 'new window')")

        title = info['event_title']
        description = info['event_details']
        location =info['event_venue']
        name = info['event_organizer_name']
        email = info['event_organizer_email']
        phone = info['event_organizer_phone_number']
        url = info['event_url']


        driver.implicitly_wait(10)
        driver.switch_to.frame("trumbaSubmitEventForm")

        try:    
                submitterNameField = driver.find_element_by_id("eaa_TextboxName")
                submitterNameField.clear()
                submitterNameField.send_keys(name)

                emailField = driver.find_element_by_id("eaa_TextboxEmail")
                emailField.clear()
                emailField.send_keys(email)

                titleField = driver.find_element_by_id("eaa_custom3_0")
                titleField.clear()
                titleField.send_keys(title)

                locationField = driver.find_element_by_id("eaa_TextboxLocation")
                locationField.clear()
                locationField.send_keys(location)

                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartMonth"))
                startMonthField.select_by_visible_text("May")
                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartDay"))
                startMonthField.select_by_visible_text("2")
                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartYear"))
                startMonthField.select_by_visible_text("2017")

                startTimeHrField = Select(driver.find_element_by_id("eaa_DropDownStartHour"))
                startTimeHrField.select_by_visible_text("11")
                startTimeMinField = Select(driver.find_element_by_id("eaa_DropDownStartMinute"))
                startTimeMinField.select_by_visible_text("20")
                startTimeField = Select(driver.find_element_by_id("eaa_DropDownStartAMPM"))
                startTimeField.select_by_visible_text("PM")

                endTimeHrField = Select(driver.find_element_by_id("eaa_DropDownEndHour"))
                endTimeHrField.select_by_visible_text("11")
                endTimeMinField = Select(driver.find_element_by_id("eaa_DropDownEndMinute"))
                endTimeMinField.select_by_visible_text("40")
                endTimeField = Select(driver.find_element_by_id("eaa_DropDownEndAMPM"))
                endTimeField.select_by_visible_text("PM")

                organizerField = driver.find_element_by_id("eaa_custom29378_0")
                organizerField.clear()
                organizerField.send_keys(name)

                nameField = driver.find_element_by_id("eaa_custom29379_0")
                nameField.clear()
                nameField.send_keys(name)

                phoneField = driver.find_element_by_id("eaa_custom29380_0")
                phoneField.clear()
                phoneField.send_keys(phone)

                emailField = driver.find_element_by_id("eaa_custom29641_0")
                emailField.clear()
                emailField.send_keys(email)

                urlField = driver.find_element_by_id("eaa_custom6_0")
                urlField.clear()
                urlField.send_keys(url)

##                descriptionField = driver.find_element_by_id("eaa_RowNotes")
##                descriptionField.send_keys(description)

##                submit = driver.find_element_by_id("eaa_buttonSubmit")
##                submit.click()
                
        except:
                websites['unsuccessful'].append("City of North Vancouver")
        else:
                websites['captcha'].append("City of North Vancouver") 

def ubyssey(info):
        driver.execute_script("window.open('https://www.ubyssey.ca/events/submit/form', 'new window')")

        title = info['event_title']
        location=info['event_venue']
        description = info['event_details']
        address = info['event_street']
        host = info['event_organizer_name']
        email = info['event_organizer_email']
        phone = info['event_organizer_phone_number']
        ticket = info['event_ticketURL']


        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_title')))
        except TimeoutException:
            print("Loading took too much time!")
            driver.quit()
        try:     
                titleField = driver.find_element_by_id("id_title")
                titleField.clear()
                titleField.send_keys(title)

                descriptionField = driver.find_element_by_id("id_description")
                descriptionField.clear()
                descriptionField.send_keys(description)

                hostField = driver.find_element_by_id("id_host")
                hostField.clear()
                hostField.send_keys(host)

                categoryField = Select(driver.find_element_by_id("id_category"))
                categoryField.select_by_visible_text("Academic")

                startTimeField = driver.find_element_by_id("id_start_time")
                startTimeField.clear()
##                startTimeField.send_keys(startTime)

                endTimeField = driver.find_element_by_id("id_end_time")
                endTimeField.clear()
##                endTimeField.send_keys(endTime)

                locationField = driver.find_element_by_id("id_location")
                locationField.clear()
                locationField.send_keys(location)

                addressField = driver.find_element_by_id("id_address")
                addressField.clear()
                addressField.send_keys(address)

                ticketField = driver.find_element_by_id("id_ticket_url")
                ticketField.clear()
                ticketField.send_keys(ticket)

                emailField = driver.find_element_by_id("id_submitter_email")
                emailField.clear()
                emailField.send_keys(email)

                phoneField = driver.find_element_by_id("id_submitter_phone")
                phoneField.clear()
                phoneField.send_keys(phone)
        except:
              websites['unsuccessful'].append("Ubyssey")
        else:
                try:
                        driver.implicitly_wait(10)
                        driver.find_element_by_id("id_ticket_url")
                        websites['unsuccessful'].append("Ubyssey")
                except NoSuchElementException:
                        websites['successful'].append("Ubyssey")


def northShore(info):
        driver.execute_script("window.open('http://www.nsnews.com/add-event', 'new window')")
        driver.switch_to.frame("trumbaSubmitEventForm");


        title = info['event_title']
        description = info['event_details']
        name = info['event_organizer_name']
        email = info['event_organizer_email']
        phone = info['event_organizer_phone_number']
        price = info['event_price']
        venue= info['event_venue']
        webLink = info['event_url']


        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'eaa_TextboxName')))
        except TimeoutException:
            print("Loading took too much time!")
            driver.quit()
        try:
                nameField = driver.find_element_by_id("eaa_TextboxName")
                nameField.clear()
                nameField.send_keys(name)

                emailField = driver.find_element_by_id("eaa_TextboxEmail")
                emailField.clear()
                emailField.send_keys(email)

                phoneField = driver.find_element_by_id("eaa_TextboxPhone")
                phoneField.clear()
                phoneField.send_keys(phone)

                titleField = driver.find_element_by_id("eaa_custom3_0")
                titleField.clear()
                titleField.send_keys(title)

                priceField = driver.find_element_by_id("eaa_custom33705_0")
                priceField.send_keys(price)

##                cityField = Select(driver.find_element_by_class_name("select2-search__field"))
##                cityField.select_by_visible_text(city)

                locationField = driver.find_element_by_id("eaa_TextboxLocation")
                locationField.send_keys(venue)
                
                descriptionField = driver.find_element_by_name("eaa$custom4_0")
                descriptionField.clear()
                descriptionField.send_keys(description)

##                startDayField = Select(driver.find_element_by_id("eaa_DropDownStartMonth"))
##                startDayField.select_by_visible_text("May")
##                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartDay"))
##                startMonthField.select_by_visible_text("2")
##                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartYear"))
##                startMonthField.select_by_visible_text("2018")
##
##                startTimeHrField = Select(driver.find_element_by_id("eaa_DropDownStartHour"))
##                startTimeHrField.select_by_visible_text("11")
##                startTimeMinField = Select(driver.find_element_by_id("eaa_DropDownStartMinute"))
##                startTimeMinField.select_by_visible_text("20")
##                startTimeField = Select(driver.find_element_by_id("eaa_DropDownStartAMPM"))
##                startTimeField.select_by_visible_text("PM")
##
##                durationField = Select(driver.find_element_by_id("eaa_DropDownDurationHours"))
##                durationField.select_by_visible_text("3 hours")

                eventTypeField = Select(driver.find_element_by_id("eaa_custom17792_0_selectedItems"))
                eventTypeField.select_by_visible_text("All ages")

                webLinkField = driver.find_element_by_id("eaa_custom6_0")
                webLinkField.clear()
                webLinkField.send_keys(webLink)

                descriptionField = driver.find_element_by_id("eaa_custom4_0")
                descriptionField.clear()
                descriptionField.send_keys(description)
        except:
              websites['unsuccessful'].append("North Shore")
        else:
                try:
                        driver.implicitly_wait(10)
                        driver.find_element_by_id("eaa_custom6_0")
                        websites['unsuccessful'].append("North Shore")
                except:
                        websites['successful'].append("North Shore")

        

def craigsList(info):
        driver.execute_script("window.open('http://post.craigslist.org/k/6LCtjvRV6BGHSA6-sDz7FA/5ViVw?lang=en&cc=us&s=edit', 'new window')")

        title = info['event_title']
        venue=info['event_venue']
        description = info['event_details']
        city = info['event_city']
        street = info['event_street']
        name = info['event_organizer_name']
        email = info['event_organizer_email']
        phone = info['event_organizer_phone_number']
        postalCode = info['event_postal_code']



        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'PostingTitle')))
        except TimeoutException:
            print("Loading took too much time!")
            driver.quit()
        try:
                titleField = driver.find_element_by_id("PostingTitle")
                titleField.clear()
                titleField.send_keys(title)

                postalCodeField = driver.find_element_by_id("postal_code")
                postalCodeField.clear()
                postalCodeField.send_keys(postalCode)

                descriptionField = driver.find_element_by_id("PostingBody")
                descriptionField.clear()
                descriptionField.send_keys(description)

                durationField = Select(driver.find_element_by_name("eventDuration"))
                durationField.select_by_index(0)

                emailField = driver.find_element_by_id("FromEMail")
                emailField.clear()
                emailField.send_keys(email)

                emailField = driver.find_element_by_id("ConfirmEMail")
                emailField.clear()
                emailField.send_keys(email)

                phoneField = driver.find_element_by_id("contact_phone")
                phoneField.clear()
                phoneField.send_keys(phone)

                streetField = driver.find_element_by_id('xstreet0')
                streetField.clear()
                streetField.send_keys(street)

                venueField = driver.find_element_by_id('venue_name')
                venueField.clear()
                venueField.send_keys(venue)

                nameField = driver.find_element_by_id('contact_name')
                nameField.send_keys(name)

                cityField = driver.find_element_by_id('city')
                cityField.clear()
                cityField.send_keys(city)
        except:
             websites['unsuccessful'].append("Craigslist")
        else:
                try:
                        driver.implicitly_wait(10)
                        driver.find_element_by_id("xstreet0")
                        websites['unsuccessful'].append("Craigslist")
                except NoSuchElementException:
                        websites['successful'].append("Craigslist")

def boredInVancouver(info):
        driver.execute_script("window.open('http://post.craigslist.org/k/6LCtjvRV6BGHSA6-sDz7FA/5ViVw?lang=en&cc=us&s=edit', 'new window')")

        title = info['event_title']
        venue=info['event_venue']
        description = info['event_details']
        name = info['event_organizer_name']
        email = info['event_organizer_email']
        url = info['event_url']

        try:
                titleField = driver.find_element_by_id("g32-nameoflisting")
                titleField.clear()
                titleField.send_keys(title)

                descriptionField = driver.find_element_by_id("contact-form-comment-g32-briefdescriptionoflistingandwemeanbrief-wehaveveryshortattentionspans")
                descriptionField.clear()
                descriptionField.send_keys(description)

                emailField = driver.find_element_by_id("g32-youremail")
                emailField.clear()
                emailField.send_keys(email)

                urlField = driver.find_element_by_id("g32-url")
                urlField.clear()
                urlField.send_keys(url)

                venueField = driver.find_element_by_id('g32-dateslocationpricinginfo')
                venueField.clear()
                venueField.send_keys(venue)

                nameField = driver.find_element_by_id('g32-yourname')
                nameField.send_keys(name)

=        except:
             websites['unsuccessful'].append("Bored In Vancouver")
        else:
                try:
                        driver.implicitly_wait(10)
                        driver.find_element_by_id("g32-yourname")
                        websites['unsuccessful'].append("Bored In Vancouver")
                except NoSuchElementException:
                        websites['successful'].append("Bored In Vancouver")
        
        
def main():
        global driver
        global username
        global password
        global info

        input = sys.argv[1]
        info = json.loads(input)

        functions = {
                "Eventful": eventful,
                "Youth Core": youthCore,
                "Planet Friendly":planetFriendly,
                "Global News": globalNews,
                "Kijiji": kijiji,
                "Metro Vancouver": metroVancouver,
                "Community of North Vancouver": cnv,
                "Ubyssey": ubyssey,
                "North Shore": northShore,
                "Craigslist": craigsList,
                "Bored in Vancouver": boredInVancouver
                }

        for website in info['event_websites']:
            try:
                functions[website](info)
            except Exception:
                pass

        print(websites)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
