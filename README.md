# SPES-PE
Automatic Event Uploader for Stanley Park Ecology Society 

![alt text](https://github.com/CodeTheChangeUBC/SPES-PE/blob/master/img.PNG)

# What you need to install

* [Node.js](https://nodejs.org/en/)
* [Python3](https://anaconda.org/anaconda/python)
* [Selenium](https://pypi.org/project/selenium/)
* [Chrome](https://www.google.com/chrome/)

# How to start
* (Windows) Double click on start.bat
* (Mac/Linux) navigate inside the app folder , type node app.js in terminal and go to localhost:8000 on your browser

# How to add more websites

### STEP 1: Add website name to the drop down menue on website
  * Go to [views/landing.html](https://github.com/CodeTheChangeUBC/SPES-PE/blob/master/App/views/landing.html#L348-L372)
  * Add the new website's name in an options tag 
  ```html 
<option value="funcName">New Website Name</option>
  ```
### STEP 2: Add new function to python script
  * Go to [scripts/script.py](https://github.com/CodeTheChangeUBC/SPES-PE/blob/master/App/views/landing.html#L33)
  * Define a new function in the following format
  ```python 
def funcName(info,handleCount):
        try:
           driver.execute_script('''window.open("http://website.com","_blank");''')
           driver.switch_to.window(driver.window_handles[handleCount])
           ## Scrape website here
        except:
            websites["unsuccessful"].append("Website Name")
        else:
            websites["successful"].append("Website Name")
  ```
  * Add the func to the [functions dictionary](https://github.com/CodeTheChangeUBC/SPES-PE/blob/master/App/views/landing.html#L94)
  ```python
          functions = {
                "Eventful": eventful,
                "Youth Core": youthCore,
                "Planet Friendly":planetFriendly,
                "Value of options field in html page" : funcName
                }
   ```
 ### STEP 3 : Celebrate the addition of the new function :boom:
 ##### Things to note , 
 * Follow the exact function pattern provided
 * Make sure that the function key in the function's dictionary matches the value in the options tag
 
