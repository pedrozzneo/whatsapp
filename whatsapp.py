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

def search(filter):
    try:
        search_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6')))
        search_field.clear()
        search_field.send_keys(filter)
        time.sleep(5)
    except Exception as e:
        print(f"Error searching: {str(e)}")

# Set chrome driver
driver = set_driver()

# Open whatsapp
driver.get("https://web.whatsapp.com")

# Set up the wait time for EC
wait = WebDriverWait(driver, 30)

# search "lista" contacts
search("carona")

# Build the list of "lista" contacts
try:
    
    # Assign all contacts to the variable with a lot of info
    # listaWebElements = wait.until(EC.presence_of_all_elements_located((
    #     By.CLASS_NAME, "_ak8l"
    # )))
    #print(f"{len(listaWebElements)} lista contacts:")

    # Array that will store ONLY the name of each contact
    # listaNames = []

    # # Extract and store the names of each contact
    # for contact in listaWebElements:
    #     contact_text = contact.text
    #     contact_name = contact_text.split('\n')[0]
    #     listaNames.append(contact_name)


    # listaWebElements = driver.find_elements(
    # By.XPATH,
    # '//div[@aria-label="Search results." and contains(@class, "x1y332i5")]/*[following-sibling::div[contains(@class, "x9f619") and contains(@class, "x1jchvi3") and contains(@class, "xtvhhri") and contains(text(), "Groups in common")]]'
    # )

    # 1. Find the parent container

    # search_results = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Search results."]')

    # wait = WebDriverWait(driver, 40)
    # children = wait.until(
    # EC.presence_of_all_elements_located((
    #     By.CSS_SELECTOR, 'div[aria-label="Search results."] > div[role="row"]'
    # ))
    # )

        # Replace the search results section with:
   
    # start_time = time.time()
    # timeout = 15  # 30 seconds timeout
    # collected_names = []
    # last_length = 0
    
    # while time.time() - start_time < timeout:
    #     # Find all currently loaded elements
    #     children = driver.find_elements(
    #         By.CSS_SELECTOR, 'div[aria-label="Search results."] > div[role="row"]'
    #     )
        
    #     # Process only new elements
    #     for child in children[last_length:]:
    #         child_text = child.text
    #         if child_text == "GROUPS IN COMMON" or child_text == "CHATS":
    #             # Exit both loops if we hit the groups marker
    #             timeout = 0  # Force outer loop to end
    #             break
            
    #         contact_name = child_text.split('\n')[0]
    #         if contact_name and contact_name not in collected_names:
    #             collected_names.append(contact_name)
        
    #     # Update last known length
    #     last_length = len(children)
        
    #     # Small sleep to prevent excessive CPU usage
    #     time.sleep(0.5)
    
    # # Remove the first item (usually the search box)
    # if collected_names:
    #     collected_names.pop(0)
    
    # print(f"Found {len(collected_names)} contacts in {time.time() - start_time:.1f} seconds:")
    # print(collected_names)

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
            # Get the text content
            # element_text = element.text.strip()
            
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
            
    print(f"Found {len(names_array)} names:")
    print(names_array)    
    # listaNames = []

    # for child in children:
    #     child_text = child.text
    #     if child_text == "GROUPS IN COMMON":
    #         print("GROUPS IN COMMON -> stop")# Replace lines 77-79 with:
    #         break
    #     contact_name = child_text.split('\n')[0]
    #     listaNames.append(contact_name)

    # listaNames.pop(0)
    # print(listaNames)
   
    # for child in children:
    #     # Check if this is the stop marker
    #     if "Groups in common" in child.text and "x9f619" in child.get_attribute("class"):
    #         break
    #     collected.append(child)
       
except TimeoutException:
    print("No titles found with the given filter within the timeout period")

# # Filter "excluir" contacts
# try:
#     # Find the search bar
#     search_field = wait.until(EC.presence_of_element_located((
#         By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6'
#     )))

#     # Enter the filter and search it
#     filter = "excluir"
#     search_field.click()
#     search_field.send_keys(filter)
#     time.sleep(5)
# except TimeoutException:
#     print("Search field not found within the given time.")

# # Build the list of "excluir" contacts
# try:
#     # Assign all contacts to the variable with a lot of info
#     excluirWebElements = wait.until(EC.presence_of_all_elements_located((
#         By.CLASS_NAME, "_ak8l"
#     )))
#     print(f"{len(excluirWebElements)} excluir contacts:")

#     # Array that will store ONLY the name of each contact
#     excluirNames = []

#     # Extract and store the names of each contact
#     for contact in excluirWebElements:
#         contact_text = contact.text
#         contact_name = contact_text.split('\n')[0]
#         excluirNames.append(contact_name)

#     print(excluirNames)
# except TimeoutException:
#     print("No titles found with the given filter within the timeout period")

# Wait to see the results

#     element.click()
#     ActionChains(driver).send_keys("ignora essa mensagem, eh teste kkkkkk").perform()
#     ActionChains(driver).send_keys(Keys.RETURN).perform()        
#     time.sleep(2)      