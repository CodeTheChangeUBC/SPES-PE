import sys,os
import time
import json
import getpass
from datetime import datetime
from selenium import webdriver
class TimeoutException(Exception): pass
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__))+'\\chromedriver.exe')
handleCount = 0
username = "ctcstanley1@gmail.com"
password = "codethechange"
websites ={"successful":[],
           "unsuccessful":[]
          }


def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)


def eventful(info,handleCount):
        try:
           title = info['event_title']
           date = info['event_date_start'][:findnth(info['event_date_start']," ",2)]
           startTime=info['event_date_start'][findnth(info['event_date_start']," ",2)+1:]
           endTime = info['event_date_end'][findnth(info['event_date_end']," ",2)+1:]
           venue=info['event_venue']
           description = info['event_details'] + "\n" + "Event Address: " + info['event_street'] + ", " + info['event_city'] + ", " + info['event_postal_code'] + "\n" + "Age group: " + \
           info['event_age_group']+ "\n" + "Organizer Contact Info: " + info['event_contact_name'] + ", " + info['event_organizer_email'] + ", " + info['event_contact_number']
           facebookURL = info['event_fbURL']
           price = info['event_price']
           link = info['event_url']
           category1 = info['event_category1'][0]

           driver.execute_script('''window.open("http://eventful.com/signin?goto=%2Fevents%2Fnew","_blank");''')
           driver.switch_to.window(driver.window_handles[handleCount])

           usernameField = driver.find_element_by_id("inp-username")
           usernameField.send_keys(username)
           passwordField = driver.find_element_by_id("inp-password")
           passwordField.send_keys(password)
           passwordField.submit()

           myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'inp-title')))

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

           categoryField = Select(driver.find_element_by_id("inp-category1"))
           categoryField.select_by_visible_text(category1)


           if len(info['event_category1']) > 1:
                categoryField2 = Select(driver.find_element_by_id("inp-category2"))
                categoryField2.select_by_visible_text(info['event_category1'][1])
                if len(info['event_category1']) == 3:
                    categoryField3 = Select(driver.find_element_by_id("inp-category3"))
                    categoryField3.select_by_visible_text(info['event_category1'][2])


               
           
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
            websites["unsuccessful"].append("Eventful")
        else:
            websites["successful"].append("Eventful")
        

def youthCore(info,handleCount):
        try:
                driver.execute_script('''window.open("http://youthcore.ca/index.php?action=create_event","_blank");''')
                driver.switch_to.window(driver.window_handles[handleCount])

                title = info['event_title']
                startTime=info['event_date_start'][findnth(info['event_date_start']," ",2)+1:]
                endTime = info['event_date_end'][findnth(info['event_date_end']," ",2)+1:]
                venue=info['event_venue']
                details = info['event_details'] + "\n" + "Event Address: " + info['event_street'] + ", " + info['event_city'] + ", " + info['event_postal_code'] + "\n" + \
                          "\n" + "Organizer Contact #: " + info['event_contact_number']+ "\n" + "Event Website: " + info['event_url'] + "\n" + \
                          "Ticket Purchasing Website: " + info['event_ticketURL']
                facebookURL = info['event_fbURL']
                cost = info['event_price']
                ageGroup = info['event_age_group']
                name = info['event_contact_name']
                email = info['event_organizer_email']        

                myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'submitter_name')))

                nameField = driver.find_element_by_id("submitter_name")
                nameField.send_keys(name)
                emailField = driver.find_element_by_id("submitter_email")
                emailField.send_keys(email)

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
                websites["unsuccessful"].append("Youth Core")
        else:
                websites["successful"].append("Youth Core")


def planetFriendly(info,handleCount):
        try:
                driver.execute_script('''window.open("http://planetfriendly.net/submit3.html","_blank");''')
                driver.switch_to.window(driver.window_handles[handleCount])

                title = info['event_title']
                s = info['event_date_start'][:findnth(info['event_date_start']," ",2)]
                s = s.replace(',', '')
                startDay = str(datetime.strptime(s,'%B %d %Y').strftime('%A'))
                startDate = info['event_date_start'][findnth(info['event_date_start']," ",0)+1:findnth(info['event_date_start'],",",0)]
                startMonth=info['event_date_start'][:findnth(info['event_date_start']," ",0)]
                if startMonth == "June" or startMonth == "July" or startMonth == "September":
                        startMonth = startMonth[:4]
                else:
                        startMonth = startMonth[:3]
                                        
                startYear = info['event_date_start'][findnth(info['event_date_start']," ",1)+1:findnth(info['event_date_start']," ",1)+5]
                description = info['event_details'] + "\n" + "Address: " + info['event_street'] + ", " + info['event_postal_code'] + "\n" + \
                              "Age Group: " + info['event_age_group'] + "\n" + "Facebook Event: " + info['event_fbURL'] + "\n" + "Price: " + info['event_price'] + "\n" + \
                              "Ticket Purchasing: " + info['event_ticketURL'] 
                city = info['event_city']
                contactName = info['event_contact_name']
                contactEmail = info['event_organizer_email']
                contactPhone = info['event_contact_number']
                contactWeb = info['event_url']
                contactWeb = contactWeb.replace('http://','')

                driver.implicitly_wait(15)
                titleField = driver.find_element_by_name("Title")
                titleField.send_keys(title)

                startDayField = Select(driver.find_element_by_name("StartDay"))
                startDayField.select_by_visible_text(startDay)

                startDateField = Select(driver.find_element_by_name("StartDate"))
                startDateField.select_by_visible_text(startDate)

                startMonthField = Select(driver.find_element_by_name("StartMonth"))
                startMonthField.select_by_visible_text(startMonth)

                startYearField = Select(driver.find_element_by_name("StartYear"))
                startYearField.select_by_visible_text(startYear)

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
                websites["successful"].append("Planet Friendly")


def globalNews(info,handleCount):
        try:
                driver.execute_script('''window.open("https://globalnews.ca/bc/events/add/","_blank");''')
                driver.switch_to.window(driver.window_handles[handleCount])

                title = info['event_title']
                venue=info['event_venue']
                description = info['event_details'] + "\n" + "Facebook Event: " + info['event_fbURL'] + "\n" + "Ticket Purchasing: "+ info['event_ticketURL'] + \
                              "\n" + "Event Price: " + info['event_price'] 
                age = info['event_age_group']
                
                startDate = info['event_date_start'][findnth(info['event_date_start']," ",0)+1:findnth(info['event_date_start'],",",0)]
                startMonth=info['event_date_start'][:findnth(info['event_date_start']," ",0)]
                startYear = info['event_date_start'][findnth(info['event_date_start']," ",1)+1:findnth(info['event_date_start']," ",1)+5]

                startHour = info['event_date_start'][findnth(info['event_date_start']," ",2)+1:findnth(info['event_date_start']," ",2)+2]
                startMinute=info['event_date_start'][findnth(info['event_date_start'],":",0)+1:findnth(info['event_date_start'],":",0)+3]
                startMinute = str(int(startMinute) - int(startMinute)%15)
                startAM=info['event_date_start'][findnth(info['event_date_start'],":",0)+4:findnth(info['event_date_start'],":",0)+6]        

                endDate = info['event_date_end'][findnth(info['event_date_end']," ",0)+1:findnth(info['event_date_end'],",",0)]
                endMonth=info['event_date_end'][:findnth(info['event_date_end']," ",0)]
                endYear = info['event_date_end'][findnth(info['event_date_end']," ",1)+1:findnth(info['event_date_end']," ",1)+5]

                endHour = info['event_date_end'][findnth(info['event_date_end']," ",2)+1:findnth(info['event_date_end']," ",2)+2]
                endMinute=info['event_date_end'][findnth(info['event_date_end'],":",0)+1:findnth(info['event_date_end'],":",0)+3]
                endMinute = str(int(endMinute) - int(endMinute)%15)
                endAM=info['event_date_end'][findnth(info['event_date_end'],":",0)+4:findnth(info['event_date_end'],":",0)+6]        

                
                city = info['event_city']
                street = info['event_street']
                organizerName = info['event_contact_name']
                organizerEmail = info['event_organizer_email']
                organizerPhone = info['event_contact_number']
                eventURL = info['event_url']
                postalCode = info['event_postal_code']
                ticketURL = info['event_ticketURL']
                category = info['event_category2']

                if startMinute == "5":
                        startMinute = "05"

                if startMinute == "0":
                        startMinute = "00"

                if endMinute == "5":
                        endMinute = "05"

                if endMinute == "0":
                        endMinute = "00"

                myElem = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, 'event-name')))

                nameField = driver.find_element_by_id("event-name")
                nameField.clear()
                nameField.send_keys(title)

                descriptionField = driver.find_element_by_id("event-description")
                descriptionField.send_keys(description)

                typeField = Select(driver.find_element_by_name("event-type"))
                typeField.select_by_visible_text(category)

                endHourField = Select(driver.find_element_by_name("event-time-hour-end"))
                endHourField.select_by_visible_text(endHour)

                endMinuteField = Select(driver.find_element_by_name("event-time-minute-end"))
                endMinuteField.select_by_visible_text(endMinute)

                endAMField = Select(driver.find_element_by_name("event-time-ampm-end"))
                endAMField.select_by_visible_text(endAM)

                endDateField = Select(driver.find_element_by_name("event-day-end"))
                endDateField.select_by_visible_text(endDate)

                endMonthField = Select(driver.find_element_by_name("event-month-end"))
                endMonthField.select_by_visible_text(endMonth)

                endYearField = Select(driver.find_element_by_name("event-year-end"))
                endYearField.select_by_visible_text(endYear)

                startHourField = Select(driver.find_element_by_name("event-time-hour-start"))
                startHourField.select_by_visible_text(startHour)

                startMinuteField = Select(driver.find_element_by_name("event-time-minute-start"))
                startMinuteField.select_by_visible_text(startMinute)

                startAMField = Select(driver.find_element_by_name("event-time-ampm-start"))
                startAMField.select_by_visible_text(startAM)

                startDateField = Select(driver.find_element_by_name("event-day-start"))
                startDateField.select_by_visible_text(startDate)

                startMonthField = Select(driver.find_element_by_name("event-month-start"))
                startMonthField.select_by_visible_text(startMonth)

                startYearField = Select(driver.find_element_by_name("event-year-start"))
                startYearField.select_by_visible_text(startYear)
                
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
                websites["unsuccessful"].append("Global News")
        else:
                websites["successful"].append("Global News")


##def kijiji(price,dateFrom,dateTo,title,description,postalCode,street,organizerPhone):
####        driver.execute_script("window.open('https://www.kijiji.ca/t-login.html?targetUrl=L3Atc2VsZWN0LWNhdGVnb3J5Lmh0bWw/Y2F0ZWdvcnlJZD0yODkmdXNlclJlZ2lzdGVyZWQ9dHJ1ZV54Tk1KeU9ySTA5U0Z3MDdzS213OC93PT0',
####                              'new window')")
##
##        try: 
##                usernameField = driver.find_element_by_id("LoginEmailOrNickname")
##        except NoSuchElementException:
##                print('Username field ID changed')
##                
##        usernameField.send_keys(username)
##
##        try:
##                passwordField = driver.find_element_by_id("login-password")
##        except NoSuchElementException:
##               print('Password field ID changed')
##
##        passwordField.send_keys(password)
##        passwordField.submit()
##
##        try:
##            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'FormLocationPicker')))
##        except TimeoutException:
##            print ("Loading took too much time!")
##
##        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "British Columbia")))
##        element.click()
##        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Greater Vancouver Area")))
##        element.click()
##        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Vancouver")))
##        element.click()
##
##        form = driver.find_element_by_id("PageSelect")
##        form.click()
##        try: 
##                priceField = driver.find_element_by_id("PriceAmount")
##                priceField.send_keys(price)
##
##                dateField = driver.find_element_by_id("SelectDate")
##                dateField.send_keys(dateFrom)
##                
##                dateToField = driver.find_element_by_id("SelectDateTo")
##                dateToField.send_keys(dateTo)
##
##                titleField = driver.find_element_by_id("postad-title")
##                titleField.send_keys(title)
##
##                descriptionField = driver.find_element_by_id("pstad-descrptn")
##                descriptionField.send_keys(description)
##
##                postalCodeField = driver.find_element_by_id("PostalCode")
##                postalCodeField.send_keys(postalCode)
##
##                streetField = driver.find_element_by_id("pstad-map-address")
##                streetField.send_keys(street)
##
##                numberField = driver.find_element_by_id("PhoneNumber")
##                numberField.send_keys(organizerPhone)
##        except:
##                websites['unsuccessful'].append("Kijiji")
##        else:
##                try:
##                        driver.implicitly_wait(10)
##                        driver.find_element_by_id("SelectDate")
##                        websites['unsuccessful'].append("Kijiji")
##                except NoSuchElementException:
##                        websites['successful'].append("Kijiji")


def metroVancouver(info,handleCount):
        try:
                title = info['event_title']
                location=info['event_venue']
                description = info['event_details'] + "\n" + "Event Address: " + info['event_street'] + ", " + info['event_postal_code'] + "\n" + \
                              "Age Group: " + info['event_age_group'] + "\n" + "Facebook Event: " + info['event_fbURL'] + "\n" + "Price: " + \
                              info['event_price'] + "\n" + "Ticket Purchasing: " + info['event_ticketURL'] 
                address = info['event_street']
                organizerName,lastName = info['event_contact_name'].split(" ")
                email = info['event_organizer_email']
                phone = info['event_contact_number']
                link = info['event_url']

                s = info['event_date_start'][:findnth(info['event_date_start']," ",2)]
                s = s.replace(',', '')
                date_obj = datetime.strptime(s, "%B %d %Y")
                startDate = str(datetime.strftime(date_obj, "%m/%d/%y"))

                s = info['event_date_end'][:findnth(info['event_date_end']," ",2)]
                s = s.replace(',', '')
                date_obj = datetime.strptime(s, "%B %d %Y")
                endDate = str(datetime.strftime(date_obj, "%m/%d/%y"))

                startHour = info['event_date_start'][findnth(info['event_date_start']," ",2)+1:findnth(info['event_date_start']," ",2)+2]
                startAM=info['event_date_start'][findnth(info['event_date_start'],":",0)+4:findnth(info['event_date_start'],":",0)+6]
                startHour = startHour + " " + startAM

                startMinute=info['event_date_start'][findnth(info['event_date_start'],":",0)+1:findnth(info['event_date_start'],":",0)+3]
                startMinute = str(int(startMinute) - int(startMinute)%5)

                if startMinute == "5":
                        startMinute = "05"

                if startMinute == "0":
                        startMinute = "00"

                endHour = info['event_date_end'][findnth(info['event_date_end']," ",2)+1:findnth(info['event_date_end']," ",2)+2]
                endAM=info['event_date_end'][findnth(info['event_date_end'],":",0)+4:findnth(info['event_date_end'],":",0)+6]        
                endHour = endHour + " " + endAM
                
                endMinute=info['event_date_end'][findnth(info['event_date_end'],":",0)+1:findnth(info['event_date_end'],":",0)+3]
                endMinute = str(int(endMinute) - int(endMinute)%5)
                if endMinute == "5":
                        endMinute = "05"

                if endMinute == "0":
                        endMinute = "00"

                driver.execute_script('''window.open("http://www.metrovancouver.org/events/Pages/add-event.aspx","_blank");''')
                driver.switch_to.window(driver.window_handles[handleCount])

                myElem = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,
                                                                                         'ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_CommentsField_ctl00_ctl00_TextField')))
                endHourField = Select(driver.find_element_by_name("ctl00$ctl35$g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718$EndDateField$ctl00$ctl00$DateTimeField$DateTimeFieldDateHours"))
                endHourField.select_by_visible_text(endHour)

                endMinuteField = Select(driver.find_element_by_name("ctl00$ctl35$g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718$EndDateField$ctl00$ctl00$DateTimeField$DateTimeFieldDateMinutes"))
                endMinuteField.select_by_visible_text(endMinute)

                startHourField = Select(driver.find_element_by_name("ctl00$ctl35$g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718$StartDateField$ctl00$ctl00$DateTimeField$DateTimeFieldDateHours"))
                startHourField.select_by_visible_text(startHour)
                      
                startMinuteField = Select(driver.find_element_by_name("ctl00$ctl35$g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718$StartDateField$ctl00$ctl00$DateTimeField$DateTimeFieldDateMinutes"))
                startMinuteField.select_by_visible_text(startMinute)

                titleField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_TitleField_ctl00_ctl00_TextField")
                titleField.send_keys(title)

                descriptionField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_CommentsField_ctl00_ctl00_TextField")
                descriptionField.send_keys(description)

                locationField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_LocationField_ctl00_ctl00_TextField")
                locationField.send_keys(location)

                addressField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_WorkAddressField_ctl00_ctl00_TextField")
                addressField.send_keys(address)

                municapility = Select(driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_MunicipalityDropDownField_ctl00_DropDownChoice"))
                municapility.select_by_visible_text("Vancouver")

                startDateField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_StartDateField_ctl00_ctl00_DateTimeField_DateTimeFieldDate")
                startDateField.clear()
                startDateField.send_keys(startDate)

                endDateField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_EndDateField_ctl00_ctl00_DateTimeField_DateTimeFieldDate")
                endDateField.clear()
                endDateField.send_keys(endDate)
                
                firstNameField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_FirstNameField_ctl00_ctl00_TextField")
                firstNameField.send_keys(organizerName)

                lastNameField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_LastNameField_ctl00_ctl00_TextField")
                lastNameField.clear()
                lastNameField.send_keys(lastName)

                phoneField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_PhoneField_ctl00_ctl00_TextField")
                phoneField.send_keys(phone)

                emailField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_EMailField_ctl00_ctl00_TextField")
                emailField.send_keys(email)

                linkField = driver.find_element_by_id("ctl00_ctl35_g_b0b67dee_6d5f_4a70_bcef_95d39f0cc718_RegistrationLinkTextField_ctl00_ctl00_TextField")
                linkField.send_keys(link)
        except:
         websites["unsuccessful"].append("Metro Vancouver")
        else:
         websites["successful"].append("Metro Vancouver")

        

def cnv(info,handleCount):
        try:
                driver.execute_script('''window.open("http://www.cnv.org/Parks-Recreation-and-Culture/Community-Events/Submit-an-Event","_blank");''')
                driver.switch_to.window(driver.window_handles[handleCount])

                title = info['event_title']
                description = info['event_details'] + "\n" + "Event Address: " +  info['event_street'] + ", " + info['event_postal_code'] + "\n" + "Age Group: " \
                               + info['event_age_group'] + "\n" + "Facebook Event: " + info['event_fbURL'] + "\n" + "Price: " + info['event_price'] + "\n" + \
                               "Ticket Purchasing: " + info['event_ticketURL'] 
                location =info['event_venue']
                name = info['event_contact_name']
                email = info['event_organizer_email']
                phone = info['event_contact_number']
                url = info['event_url']

                startDate = info['event_date_start'][findnth(info['event_date_start']," ",0)+1:findnth(info['event_date_start'],",",0)]
                startMonth=info['event_date_start'][:findnth(info['event_date_start']," ",0)]
                startYear = info['event_date_start'][findnth(info['event_date_start']," ",1)+1:findnth(info['event_date_start']," ",1)+5]

                startHour = info['event_date_start'][findnth(info['event_date_start']," ",2)+1:findnth(info['event_date_start']," ",2)+2]
                startMinute=info['event_date_start'][findnth(info['event_date_start'],":",0)+1:findnth(info['event_date_start'],":",0)+3]
                startMinute = str(int(startMinute) - int(startMinute)%15)
                if startMinute == "5":
                        startMinute = "05"

                if startMinute == "0":
                        startMinute = "00"

                startAM=info['event_date_start'][findnth(info['event_date_start'],":",0)+4:findnth(info['event_date_start'],":",0)+6]        

                endHour = info['event_date_end'][findnth(info['event_date_end']," ",2)+1:findnth(info['event_date_end']," ",2)+2]
                endMinute=info['event_date_end'][findnth(info['event_date_end'],":",0)+1:findnth(info['event_date_end'],":",0)+3]
                endMinute = str(int(endMinute) - int(endMinute)%15)
                if endMinute == "5":
                        endMinute = "05"

                if endMinute == "0":
                        endMinute = "00"

                endAM=info['event_date_end'][findnth(info['event_date_end'],":",0)+4:findnth(info['event_date_end'],":",0)+6]        



                driver.implicitly_wait(10)
                driver.switch_to.frame("trumbaSubmitEventForm")

                myElem = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,'eaa_TextboxName')))
                submitterNameField = driver.find_element_by_id("eaa_TextboxName")
                submitterNameField.clear()
                submitterNameField.send_keys(name)

                emailField = driver.find_element_by_id("eaa_TextboxEmail")
                emailField.clear()
                emailField.send_keys(email)

                titleField = driver.find_element_by_id("eaa_custom3_0")
                titleField.clear()
                titleField.send_keys(title)

                phoneField = driver.find_element_by_id("eaa_TextboxPhone")
                phoneField.clear()
                phoneField.send_keys(phone)

                locationField = driver.find_element_by_id("eaa_TextboxLocation")
                locationField.clear()
                locationField.send_keys(location)

                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartMonth"))
                startMonthField.select_by_visible_text(startMonth)
                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartDay"))
                startMonthField.select_by_visible_text(startDate)
                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartYear"))
                startMonthField.select_by_visible_text(startYear)

                startTimeHrField = Select(driver.find_element_by_id("eaa_DropDownStartHour"))
                startTimeHrField.select_by_visible_text(startHour)
                startTimeMinField = Select(driver.find_element_by_id("eaa_DropDownStartMinute"))
                startTimeMinField.select_by_visible_text(startMinute)
                startTimeField = Select(driver.find_element_by_id("eaa_DropDownStartAMPM"))
                startTimeField.select_by_visible_text(startAM)

                endTimeHrField = Select(driver.find_element_by_id("eaa_DropDownEndHour"))
                endTimeHrField.select_by_visible_text(endHour)
                endTimeMinField = Select(driver.find_element_by_id("eaa_DropDownEndMinute"))
                endTimeMinField.select_by_visible_text(endMinute)
                endTimeField = Select(driver.find_element_by_id("eaa_DropDownEndAMPM"))
                endTimeField.select_by_visible_text(endAM)

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

##                descriptionField = driver.find_element_by_id("eaa_custom4_0")
##                descriptionField.send_keys(description)

##                submit = driver.find_element_by_id("eaa_buttonSubmit")
##                submit.click()
                
        except:
                websites["unsuccessful"].append("City of North Vancouver")
        else:
                websites["successful"].append("City of North Vancouver") 

def ubyssey(info,handleCount):
        try:
                driver.execute_script('''window.open("https://www.ubyssey.ca/events/submit/form","_blank");''')
                driver.switch_to.window(driver.window_handles[handleCount])

                title = info['event_title']
                location=info['event_venue']
                description = info['event_details'] + "\n" + "Event Address: " + info['event_street'] + ", " + info['event_postal_code'] + "\n" + \
                              "Age Group: " + info['event_age_group'] + "\n" + "Facebook Event: " + info['event_fbURL'] + "\n" + "Price: " + info['event_price'] 
                address = info['event_street']
                host = info['event_contact_name']
                email = info['event_organizer_email']
                phone = info['event_contact_number']
                ticket = info['event_ticketURL']
                startTime = info['event_date_start']
                endTime = info['event_date_end']
                category = info['event_category3']

                s = info['event_date_start'][:findnth(info['event_date_start']," ",2)]
                s = s.replace(',', '')
                date_obj = datetime.strptime(s, "%B %d %Y")
                time = info['event_date_start'][findnth(info['event_date_start']," ",2)+1:]
                time = str(datetime.strptime(time, '%I:%M %p'))
                time = time[findnth(time," ",0)+1:findnth(time,":",1)]
                startDate = str(datetime.strftime(date_obj, "%y-%m-%d")) + " " + time

                s = info['event_date_end'][:findnth(info['event_date_end']," ",2)]
                s = s.replace(',', '')
                date_obj = datetime.strptime(s, "%B %d %Y")
                time = info['event_date_end'][findnth(info['event_date_end']," ",2)+1:]
                time = str(datetime.strptime(time, '%I:%M %p'))
                time = time[findnth(time," ",0)+1:findnth(time,":",1)]
                endDate = str(datetime.strftime(date_obj, "%y-%m-%d")) + " " + time


                myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'id_title')))
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
                categoryField.select_by_visible_text(category)

                startTimeField = driver.find_element_by_id("id_start_time")
                startTimeField.clear()
                startTimeField.send_keys(startDate)

                endTimeField = driver.find_element_by_id("id_end_time")
                endTimeField.clear()
                endTimeField.send_keys(endDate)

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
                websites["unsuccessful"].append("Ubyssey")
        else:
                websites["successful"].append("Ubyssey")


def northShore(info,handleCount):
        try:
                driver.execute_script('''window.open("http://www.nsnews.com/add-event","_blank");''')
                driver.switch_to.window(driver.window_handles[handleCount])

                time.sleep(15)
                driver.switch_to.frame("trumbaSubmitEventForm")

                title = info['event_title']
                description = info['event_details'] + "\n" + "Event Address: " + info['event_street'] + ", " + info['event_postal_code'] + "\n" + "Age Group: " \
                               + info['event_age_group'] + "\n" + "Facebook Event: "+ info['event_fbURL'] + "\n" + "Ticket Purchasing: " + info['event_ticketURL']
                name = info['event_contact_name']
                email = info['event_organizer_email']
                phone = info['event_contact_number']
                price = info['event_price']
                venue= info['event_venue']
                webLink = info['event_url']
                city=info['event_city']
                startDate = info['event_date_start'][findnth(info['event_date_start']," ",0)+1:findnth(info['event_date_start'],",",0)]
                startMonth=info['event_date_start'][:findnth(info['event_date_start']," ",0)]
                startYear = info['event_date_start'][findnth(info['event_date_start']," ",1)+1:findnth(info['event_date_start']," ",1)+5]

                startHour = info['event_date_start'][findnth(info['event_date_start']," ",2)+1:findnth(info['event_date_start']," ",2)+2]
                startMinute=info['event_date_start'][findnth(info['event_date_start'],":",0)+1:findnth(info['event_date_start'],":",0)+3]
                startMinute = str(int(startMinute) - int(startMinute)%5)
                startAM=info['event_date_start'][findnth(info['event_date_start'],":",0)+4:findnth(info['event_date_start'],":",0)+6]

                endDate = info['event_date_end'][findnth(info['event_date_end']," ",0)+1:findnth(info['event_date_end'],",",0)]
                endMonth=info['event_date_end'][:findnth(info['event_date_end']," ",0)]
                endYear = info['event_date_end'][findnth(info['event_date_end']," ",1)+1:findnth(info['event_date_end']," ",1)+5]

                endHour = info['event_date_end'][findnth(info['event_date_end']," ",2)+1:findnth(info['event_date_end']," ",2)+2]
                endMinute=info['event_date_end'][findnth(info['event_date_end'],":",0)+1:findnth(info['event_date_end'],":",0)+3]
                endMinute = str(int(endMinute) - int(endMinute)%15)
                endAM=info['event_date_end'][findnth(info['event_date_end'],":",0)+4:findnth(info['event_date_end'],":",0)+6]        

                if startMinute == "5":
                        startMinute = "05"

                if startMinute == "0":
                        startMinute = "00"

                if endMinute == "5":
                        endMinute = "05"

                if endMinute == "0":
                        endMinute = "00"

                myElem = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, 'eaa_custom3_0')))

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

                startDayField = Select(driver.find_element_by_id("eaa_DropDownStartMonth"))
                startDayField.select_by_visible_text(startMonth)
                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartDay"))
                startMonthField.select_by_visible_text(startDate)
                startMonthField = Select(driver.find_element_by_id("eaa_DropDownStartYear"))
                startMonthField.select_by_visible_text(startYear)

                startTimeHrField = Select(driver.find_element_by_id("eaa_DropDownStartHour"))
                startTimeHrField.select_by_visible_text(startHour)
                startTimeMinField = Select(driver.find_element_by_id("eaa_DropDownStartMinute"))
                startTimeMinField.select_by_visible_text(startMinute)
                startTimeField = Select(driver.find_element_by_id("eaa_DropDownStartAMPM"))
                startTimeField.select_by_visible_text(startAM)

                endField = driver.find_element_by_class_name("usertimezonestring")
                endField.click()

##                eventTypeField = Select(driver.find_element_by_id("eaa_custom17792_0_selectedItems"))
##                eventTypeField.select_by_visible_text("All ages")

                webLinkField = driver.find_element_by_id("eaa_custom6_0")
                webLinkField.clear()
                webLinkField.send_keys(webLink)

                descriptionField = driver.find_element_by_id("eaa_custom4_0")
                descriptionField.clear()
                descriptionField.send_keys(description)
        except:
              websites["unsuccessful"].append("North Shore")
        else:
              websites["successful"].append("North Shore")

        

def craigsList(info,handleCount):
            try:
                driver.execute_script('''window.open("http://post.craigslist.org/k/6LCtjvRV6BGHSA6-sDz7FA/5ViVw?lang=en&cc=us&s=edit","_blank");''')
                driver.switch_to.window(driver.window_handles[handleCount])

                title = info['event_title']
                venue=info['event_venue']
                description = info['event_details'] + "\n" + "Event Address: " + info['event_street'] + ", " + info['event_postal_code'] + "\n" + "Age Group: " \
                               + info['event_age_group'] + "\n" + "Facebook Event: " + info['event_fbURL'] + "\n" + "Ticket Purchasing: " +  info['event_ticketURL'] + "\n" + \
                               "Price: " + info['event_price']
                city = info['event_city']
                street = info['event_street']
                name = info['event_contact_name']
                email = info['event_organizer_email']
                phone = info['event_contact_number']
                postalCode = info['event_postal_code']
                s = info['event_date_start'][:findnth(info['event_date_start']," ",2)]
                s = s.replace(',', '')
                startDay = str(datetime.strptime(s,'%B %d %Y').strftime('%A'))
                startDay = startDay[:3]
                startDate = startDay + "," + info['event_date_start'][findnth(info['event_date_start']," ",0):findnth(info['event_date_start'],",",0)] + \
                            " " + info['event_date_start'][:findnth(info['event_date_start']," ",0)] + \
                            " " + info['event_date_start'][findnth(info['event_date_start']," ",1) +1:findnth(info['event_date_start']," ",1)+5]

                myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'PostingTitle')))
                titleField = driver.find_element_by_id("PostingTitle")
                titleField.clear()
                titleField.send_keys(title)

                postalCodeField = driver.find_element_by_id("postal_code")
                postalCodeField.clear()
                postalCodeField.send_keys(postalCode)

                dateField = driver.find_element_by_id("eventStart_js")
                dateField.clear()
                dateField.send_keys(startDate)

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
                nameField.clear()
                nameField.send_keys(name)

                cityField = driver.find_element_by_id('city')
                cityField.clear()
                cityField.send_keys(city)
            except:
             websites["unsuccessful"].append("Craigslist")
            else:
             websites["successful"].append("Craigslist")

def boredInVancouver(info,handleCount):
        try:
                driver.execute_script('''window.open("http://boredinvancouver.com/contact-us/","_blank");''')
                driver.switch_to.window(driver.window_handles[handleCount])
                
                title = info['event_title']
                venue= info['event_venue'] + ", " + info['event_date_start']+ ", " +info['event_price']
                description = info['event_details'] + "\n" + "Address: " + info['event_street'] + ", " + info['event_postal_code'] + "\n" + "Age Group: " \
                               + info['event_age_group'] + "\n" + "Facebook Event: " +  info['event_fbURL'] + "\n" + "Ticket Purchasing: " + info['event_ticketURL'] + \
                              "\n" + "Price: " + info['event_price'] + "\n" + "Contact Number: " + info['event_contact_number']
                name = info['event_contact_name']
                email = info['event_organizer_email']
                url = info['event_url']

                driver.implicitly_wait(10)
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

        except:
             websites["unsuccessful"].append("Bored In Vancouver")
        else:
             websites["successful"].append("Bored In Vancouver")
        
        
def main():
        global driver
        global username
        global password
        global info
        global handleCount
        
        input = sys.argv[1]
        info = json.loads(input)

##        f = open('C:/Users/Nadeem AbdelAziz/Desktop/Extracurriculars/sample.json', "r")
##        s = f.read()
##        info = json.loads(s)


        functions = {
                "Eventful": eventful,
                "Youth Core": youthCore,
                "Planet Friendly":planetFriendly,
                "Global News": globalNews,
##                "Kijiji": kijiji,
                "Metro Vancouver": metroVancouver,
                "City of North Van Community": cnv,
                "Ubyssey": ubyssey,
                "North Shore": northShore,
                "Craigslist": craigsList,
                "Bored In Vancouver": boredInVancouver
                }

        for website in info['event_websites']:
            try:
                handleCount+=1
                functions[website](info,handleCount)
            except:
                pass


        sys.stdout.flush()
        print(json.dumps(websites))
        sys.stdout.flush()
##        quit()



if __name__ == "__main__":
    main()
