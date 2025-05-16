from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def set_driver():
    # Create chrome options object
    chrome_options = Options()

    # Set the options for Chrome
    selenium_data_dir = os.path.join(os.path.expanduser('~'), 'selenium-chrome-data') 
    chrome_options.add_argument(f'user-data-dir={selenium_data_dir}')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-gpu')  
    chrome_options.add_argument('--start-maximized')

    return webdriver.Chrome(options=chrome_options)

def filter(filter):
    try:
        search_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6')))
        search_field.clear()
        search_field.send_keys(filter)
        time.sleep(5)
    except Exception as e:
        print(f"Error searching: {str(e)}")

def search(driver):
    names_array = []
    i = 2
    while True:
        try:
            # Try to find element at current index
            xpath = f"(//div[@class='x10l6tqk xh8yej3 x1g42fcv'])[{i}]"
            element = driver.find_element(By.XPATH, xpath)
            # Get only the first line of text
            element_text = element.text.split('\n')[0].strip()
            print(element_text)
            names_array.append(element_text)

            # Check for stop conditions
            # if element_text in ["GROUPS IN COMMON", "CHATS", "MESSAGES"]:
            #     print(f"Stop condition found: {element_text}")
            #     break
                
            # If not a stop condition, add to array
            # if element_text:
            #     names_array.append(element_text)
                
            i += 1
        except NoSuchElementException:
            print(f"No more elements found after index {i}")
            break
        except Exception as e:
            print(f"Error at index {i}: {str(e)}")
            break
            
    print(f"Found {i - 2} names:")
    return names_array

def scroll_inside_div_js(driver):
    # Find the div element
    div_element = driver.find_element(By.ID, "pane-side")
    scroll_amount=500
    num_scrolls=1

    for _ in range(num_scrolls):
        driver.execute_script(
            "arguments[0].scrollTop += arguments[1];",
            div_element,
            scroll_amount
        )
        time.sleep(0.1)  # Add a small delay between scrolls

# Set chrome driver and open whatsapp
driver = set_driver()
driver.get("https://web.whatsapp.com")

# Set up the wait time for EC
wait = WebDriverWait(driver, 30)

# filter "lista" contacts
filter("fibra")

# Build the list of "lista" contacts
names_array = []
names_array.append(search(driver))
print(names_array)   

scroll_inside_div_js(driver)  # Scrolls down one "tick"
time.sleep(5)
names_array.append(search(driver))
print(names_array)   
time.sleep(60)


#     element.click()
#     ActionChains(driver).send_keys("ignora essa mensagem, eh teste kkkkkk").perform()
#     ActionChains(driver).send_keys(Keys.RETURN).perform()        
#     time.sleep(2)      