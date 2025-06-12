import time
import driver as d
import utils
import list

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

time.sleep(10)

# Build all the lists
addedContacts, removedContacts, errors, equalNames= list.build(driver)

answer = input("wanna start from a specific contact? ")
if answer == "y":
    contact = input("enter the exact name of the contact: ")
    addedContacts = list.filter(addedContacts, contact)

# Print them
utils.show(addedContacts, removedContacts, errors, equalNames)

# message each contact
#list.message(driver, addedContacts)  
