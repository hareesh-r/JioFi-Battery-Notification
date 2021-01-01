import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()

win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

import time 

from plyer import notification

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

try:

    options = Options()

    options.headless = True

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    driver.minimize_window()

    driver.get('http://jiofi.local.html/')

    driver.implicitly_wait(300)

    btn1 = driver.find_element_by_xpath('//*[@id="to_st_dev"]/a')

    btn1.click()
        
except:

    driver.close()

    notification.notify( 
            app_name = "Battery Alert app" ,
            app_icon = "D:\LEARNING\py progs\Jio\icon.ico",
            ticker = "Jio Battery Alert!!",
            title = "Jio Battery Alert!!", 
            message = "Something went wrong" , 
            timeout = 10,
            )

def findPercent():

    while True:

        percentage = driver.find_element_by_xpath('//*[@id="input_battery_level"]')

        batteryPercentage = percentage.get_attribute("value").strip()

        print(batteryPercentage)

        try:

            manipulatedBatteryPercentage = int(batteryPercentage[:-1])

        except:

            print(batteryPercentage)

            findPercent()

        if batteryPercentage == "100%":

            batteryPercentage = "Battery Got Fully Charged !!"
        
        elif manipulatedBatteryPercentage < 15:

            batteryPercentage = "Battery Percent is very low " + str(batteryPercentage)

        elif manipulatedBatteryPercentage > 15:

            batteryPercentage = "The Current Battery Percentage is "+str(batteryPercentage)

        else:

            batteryPercentage = "Wifi is not Connected with Hareesh's Jio wifi"

        notification.notify( 
            app_name = "Battery Alert app" ,
            app_icon = "D:\LEARNING\py progs\Jio\icon.ico",
            ticker = "Jio Battery Alert!!",
            title = "Jio Battery Alert!!", 
            message = batteryPercentage , 
            timeout = 10,
            )

        time.sleep(300)

findPercent()

driver.close()

# pip install -r requirements.txt
# pip freeze > requirements.txt