from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
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

def search(filter):
    try:
        search_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6')))
        search_field.clear()
        search_field.send_keys(filter)
        time.sleep(5)
    except Exception as e:
        print(f"Error searching: {str(e)}")

def build_list(driver):
    names_array = []
    i = 2
    while True:
        try:
            # Try to find element at current index
            element = driver.find_element(By.XPATH, f"(//div[@class='x10l6tqk xh8yej3 x1g42fcv'])[{i}]")
            # Get only the first line of text
            element_text = element.text.split('\n')[0].strip()
            names_array.append(element_text)

            # Check for stop conditions
            # if element_text in ["GROUPS IN COMMON", "CHATS", "MESSAGES"]:
            #     print(f"Stop condition found: {element_text}")
            #     break
                
            # If not a stop condition, add to array
            # if element_text:
            #     names_array.append(element_text)
                
            i += 1
        except Exception as e:
            print(f"Error at index {i}: {str(e)}")
            break
            
    print(f"Found {i} names:")
    return names_array

def scroll_inside_div_js(driver):
    # Find the div element
    #I NEED TO CHANGE IT SO EXACTLY WHEN THE ELEMENT GOES STALE TO GET NEW ONES PERHAPS
    div_element = driver.find_element(By.ID, "pane-side")
    scroll_amount=1550
    num_scrolls=1

    for _ in range(num_scrolls):
        driver.execute_script(
            "arguments[0].scrollTop += arguments[1];",
            div_element,
            scroll_amount
        )
        time.sleep(1)  # Add a small delay between scrolls

# Set chrome driver and open whatsapp
driver = set_driver()
driver.get("https://web.whatsapp.com")
time.sleep(20)
# Set up the wait time for EC
wait = WebDriverWait(driver, 30)

# filter "lista" contacts
search("fibra")
time.sleep(1)

final_names_array = []
i = 0
while i < 20:
    i = i + 1
    # Build the list of "lista" contacts
    scroll_inside_div_js(driver)  # Scrolls down one "tick"
    final_names_array.append(build_list(driver))   


for array in final_names_array:
    print(array)
    print("\n")

previous_array = []
i = 1
for array in final_names_array:
    if previous_array:
        position = -1
        for prev in previous_array:
            position += 1
            if array[0] == prev:
                print(f"{i} - Match found at position: {position}")
                position += 1
                continue
    i = i + 1
    previous_array = array

driver.quit()


#     element.click()
#     ActionChains(driver).send_
# keys("ignora essa mensagem, eh teste kkkkkk").perform()
#     ActionChains(driver).send_keys(Keys.RETURN).perform()        
#     time.sleep(2)      