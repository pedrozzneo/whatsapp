import time
import driver as d
import utils
import list

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# Set chrome driver and open whatsapp
driver = d.set()
driver.get("https://web.whatsapp.com")

time.sleep(10)

# Find the right contact reference and click it
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"(//div[@class='x10l6tqk xh8yej3 x1g42fcv'])[{2}]"))
)
element.click()
print("select chat")

time.sleep(10)

# Make the input field empty
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

# Select a picture on the chat
ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
print("prepare the picture")

# Click the send button
send_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Send"]'))
)
send_button.click()
print("send button click")

time.sleep(10)


# filter "lista" contacts until it is successfull
# success = False
# while not success:
#     try:
#         utils.search("fibra", driver)
#         success = True
#     except:
#         continue

# #Build the all the lists
# addedContacts, removedContacts, errors = list.build(driver)

# # Print them
# list.show(addedContacts, removedContacts, errors)

# # message each contact
# list.message(driver, addedContacts)  