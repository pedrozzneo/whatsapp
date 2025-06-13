from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def search(filter, driver):
    try:
        # Find and select the search field 
        search_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="x1hx0egp x6ikm8r x1odjw0f x6prxxf x1k6rcq7 x1whj5v"]')))
        search_field.click()
    
        # Clear the search field and type the filter
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        search_field.send_keys(Keys.BACKSPACE + filter) 
        print(f"\n Search {filter}")
    except:
        print(f"\n ❌ Search {filter}")
        raise

def scroll_inside_div_js(driver, scroll_amount):
    try:
        # Find the div element that will be scrolled
        div_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "pane-side")))

        # scroll
        driver.execute_script("arguments[0].scrollTop += arguments[1];",div_element,scroll_amount)
        print("scrolled down")
    except:
        print("❌ scrolled down")

def show(addedContacts, removedContacts, errors, equalNames):
    # Show the added contacts collected
    print(f"\n list of contacts added: \n")
    for i, contact in enumerate(addedContacts, start=1):
        print(f"{i}: {contact}")

    # Show the deleted collected 
    print(f"\n list of contacts removed: \n")
    for i, contact in enumerate(removedContacts, start=1):
        print(f"{i}: {contact}")

    # Show the errors collected
    if errors:
        print(f"\n list of errors: \n")
        for error in errors:
            print(error)
    else:
        print("\n No errors found. \n")

    if equalNames:
        print(f"\n list of equal names: \n")
        for name in equalNames:
            print(name)
    else:
        print("\n No equal names. \n")

    