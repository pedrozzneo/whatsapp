from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
from selenium.common.exceptions import TimeoutException
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

driver = set_driver()
# Open whatsapp
driver.get("https://web.whatsapp.com")

# Set up the wait time for EC
wait = WebDriverWait(driver, 30)

# Filter "lista de transmissao" contacts
try:
    # Find the search bar
    search_field = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, 'p.selectable-text.copyable-text.x15bjb6t.x1n2onr6'
    )))

    # Enter the filter and search it
    filter = "lista"
    search_field.click()
    search_field.send_keys(filter)
    time.sleep(5)
except TimeoutException:
    print("Search field not found within the given time.")

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
    search_results = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Search results."]')

    # 2. Get all direct children (or use .find_elements for specific tags)
    children = search_results.find_elements(By.XPATH, './*')
    
    listaNames = []

    for child in children:
        child_text = child.text
        if child_text == "GROUPS IN COMMON":
            print("GROUPS IN COMMON -> stop")
            break
        contact_name = child_text.split('\n')[0]
        listaNames.append(contact_name)

    listaNames.pop(0)
    print(listaNames)
   
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
time.sleep(120)

#     element.click()
#     ActionChains(driver).send_keys("ignora essa mensagem, eh teste kkkkkk").perform()
#     ActionChains(driver).send_keys(Keys.RETURN).perform()        
#     time.sleep(2)      