from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from password_generator import PasswordGenerator
import names
from random import randint, randrange


# Replace with your actual email and password


# Set the path to your ChromeDriver
driver_path = "path/to/chromedriver"  # Download from https://chromedriver.chromium.org/

def rektScammer():
    email = names.get_first_name().lower() + "@gmail.com"
    pwo = PasswordGenerator()
    password = pwo.generate()
    otp = randint(100000, 999999)



  # Open the webpage
    driver.get("https://mychoicevote.site/inst/66a09ebbfd20b70252dcca3c")

    # Find email element and enter email
    email_field = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "username"))  # Replace with appropriate locator
    )
    email_field.send_keys(email)

    # Find password element and enter password
    password_field = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "password"))  # Replace with appropriate locator
    )
    password_field.send_keys(password)

    # Find submit button and click
    submit_button = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.ID, "submit"))  # Replace with appropriate locator
    )
    submit_button.click()

    otp_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "code"))  # Replace with appropriate locator
    )

    otp_field.send_keys(otp)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))  # Replace with appropriate locator
    )
    submit_button.click()



# Initialize Chrome driver




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Chrome()
    count = 0

    # Login to the webpage
    while True:
        rektScammer()
        count+=1
        print(count)

    # You can add further actions here after successful login (optional)

    # Close the browser window
    # driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
