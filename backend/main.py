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

# Filter "lista" contacts until it's successfull
success = False
while not success:
    try:
        utils.search("fibra", driver)
        success = True
    except:
        continue

# Build all the lists
addedContacts, removedContacts, errors = list.build(driver)

# Print them
utils.show(addedContacts, removedContacts, errors)

# message each contact
list.message(driver, addedContacts)  