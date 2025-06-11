import time
import driver as d
import utils
import list


# Set chrome driver and open whatsapp
driver = d.set()
driver.get("https://web.whatsapp.com")
time.sleep(10)

# filter "lista" contacts
utils.search("fibra", driver)
# Build the all the lists
addedContacts, removedContacts, errors = list.build(driver)

# Print them
list.show(addedContacts, removedContacts, errors)

# message each contact
#list.message(driver, addedContacts)
 

#ActionChains(driver).send_keys(Keys.RETURN).perform()     