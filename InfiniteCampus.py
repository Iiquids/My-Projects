from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
import json
import requests
import datetime

url = "https://middletowncityschools.infinitecampus.org/campus/resources/portal/roster?_expand=%7BsectionPlacements-%7Bterm%7D%7D&_date=" + datetime.datetime.now().strftime("%Y-%m-%d")

# URL of the login page
login_url = 'https://middletowncityschools.infinitecampus.org/campus/portal/students/mcsd.jsp'

# Your login credentials
username = 'USERNAME'
password = 'PASSWORD'

# Start a virtual display (headless mode)
display = Display(visible=0, size=(1920, 1080))
display.start()

# Create a new instance of the Firefox driver in headless mode
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

try:
    # Open the login page
    driver.get(login_url)

    # Find the username and password input fields and fill in the information
    username_input = driver.find_element("id", "username")
    password_input = driver.find_element("id", "password")

    username_input.send_keys(username)
    password_input.send_keys(password)

    # You may need to simulate pressing Enter to submit the form, depending on the website
    password_input.send_keys(Keys.RETURN)

    # Use WebDriverWait to wait for a specific condition (in this case, the presence of an element with ID "main-workspace")
    wait = WebDriverWait(driver, 10)
    element_present = EC.presence_of_element_located((By.ID, 'main-workspace'))
    wait.until(element_present)

    iframe_element = driver.find_element(By.ID, 'main-workspace')

    # Switch to the iframe
    driver.switch_to.frame(iframe_element)

    wait = WebDriverWait(driver, 10)
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'home-collapsible-card__text-container'))
    wait.until(element_present)

    XYDAY = "/html/body/app-root/ng-component/app-home/app-portal-page/div[2]/app-payments-cart/div[2]/div/div[1]/infinite-scroll/app-schedule-today/app-collapsible-card/div/div[1]/div/app-schedule-card/div/table/caption/div/div[2]/span"
    markingPeriod = "/html/body/app-root/ng-component/app-home/app-portal-page/div[2]/app-payments-cart/div[2]/div/div[1]/infinite-scroll/app-schedule-today/app-collapsible-card/div/div[1]/div/app-schedule-card/div/table/caption/div/div[1]/span[1]"
    
    jsonFanale = {}

    mPElement = driver.find_element(By.XPATH, markingPeriod)
    term = mPElement.get_attribute("innerHTML")[19:22]

    XYElement = driver.find_element(By.XPATH, XYDAY)
    day = XYElement.get_attribute("innerHTML")[5:6]

    cooks = driver.get_cookies()

    cookies = {}

    for i in range(0, len(cooks)):
        cookies[cooks[i]["name"]] = cooks[i]["value"]


    headers = {
        "Content-Type": "application/json",
        "Cookie": "; ".join([f"{name}={value}" for name, value in cookies.items()]),
    }

    response = requests.get(url, headers=headers)
    jsonFanale["json"] = response.json()
    jsonFanale["term"] = term
    jsonFanale["day"] = day
    
    print(json.dumps(jsonFanale))

finally:
    # Switch back to the main content if needed
    driver.switch_to.default_content()

    # Close the browser and virtual display
    driver.quit()
    display.stop()
