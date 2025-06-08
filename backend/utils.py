from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def clear_search_field(driver):
    try:
        search_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6')))
        search_field.send_keys(Keys.BACKSPACE * 50)  # Clear the search field
    except Exception as e:
        print(f"Error clearing search field: {str(e)}")

def search(filter, driver):
    try:
        search_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6')))
        search_field.send_keys(filter)
    except Exception as e:
        print(f"Error searching: {str(e)}")

def scroll_inside_div_js(driver, scroll_amount):
    # Find the div element
    div_element = driver.find_element(By.ID, "pane-side")

    driver.execute_script("arguments[0].scrollTop += arguments[1];",div_element,scroll_amount)
    time.sleep(1)  # Add a small delay between scrolls
