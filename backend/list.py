from selenium.webdriver.common.by import By
import utils
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def filter(addedContacts, filter):
    while True:
        contact = addedContacts.pop(0)
        if contact == filter:
            addedContacts.append(contact)
            return addedContacts

def message(driver, addedContacts):
    i = 0
    while addedContacts != []:
        try:
            # Get the first contact in the list
            contact = addedContacts.pop(0)

            # Search for the contact
            utils.search(contact, driver)

            # Find the right contact reference and click it
            reference = 2
            name = []
            while name != contact:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"(//div[@class='x10l6tqk xh8yej3 x1g42fcv'])[{reference}]"))
                )
                name = element.text.split('\n')[0].strip()
                reference += 1
                
                # 10 is the maximum attemps
                if reference == 10:
                    element = None
                    break

            element.click()
            print("select chat")
            
            # Make the input field empty
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

            # Select a picture on the chat
            # ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            # print("prepare the picture")

            # Click the send button
            # send_button = WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Send"]'))
            # )
            #send_button.click()
            # print("send button click")

            #Type the message in the input field
            message = "Bom dia!! Tudo bem? Estamos com condições especiais nas fibras, gostaria de saber mais?"
            ActionChains(driver).send_keys(message).perform()

            #Send the message
            #ActionChains(driver).send_keys(Keys.RETURN).perform()
            
            # Save and output progress
            i += 1
            print(f"message contact {contact} - {i} succeded, there are {len(addedContacts)} left")
        except:
            # Log the error
            print(f"Error messaging contact: {contact}")

            # Re-add the contact to the list for retry
            addedContacts.append(contact) 
            continue

def build(driver):
    addedContacts = []
    removedContacts = []
    errors = []
    equalNames = []
    groupCount = 0

    # variable that determines the end of the loop
    end = False

    # The scroll amount only for the first iteration
    scroll_amount= 72 * 27 

    # Scrolls to fit perfectly the "lista" contacts
    utils.scroll_inside_div_js(driver, 243)

    while not end:
        # Find the group of contacts
        try:
            # log
            groupCount += 1
            print(f"\ncollecting contacts from group {groupCount} ... \n")

            # The list is loaded each 25 itens because of page size
            group = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, "(//div[@class='x10l6tqk xh8yej3 x1g42fcv'])")))
            print(f"size of the group: {len(group)}")
        except Exception as e:
            print(f" ❌ unable to find a group of contacts {str(e)}")
            errors.append("unable to find a group of contacts")
        
        # Transfer the names of the group to the array
        for i in range(0,24):
            try:
                name = group[i].text.split('\n')[0].strip()
            except:
                print("❌ unable to interact with contact")
                errors.append("unable to interact with contact")
                continue

            # Check for stop condition
            if name == "MESSAGES":
                # Signalize the end of the loop
                end = True
                print("MESSAGES found, stop looking for other contacts")
                break

            # Check if the contact should not be added
            if "excluir" in name.lower() or name == "CONTACTS" or name == "CHATS":
                # Show the contact that will be skipped
                print(f"skipping contact: {name}")

                # Add the contact to the removed contacts array for further check
                removedContacts.append(name)
                continue
        
            # Add the contact to the array only if its new
            if name not in addedContacts:
                addedContacts.append(name)    
                print(f" {name} added")
            else:
                equalNames.append(name)
                print(f" {name} already on list")

        # Quit the loop
        if end:
            print("End of contacts reached.")
            break

        # Get ready for the next iteration
        utils.scroll_inside_div_js(driver, scroll_amount)

        # Wait for the DOM to make this instance stale, giving room for the new one
        WebDriverWait(driver, 30).until(EC.staleness_of(group[0]))
        print("Old group become stale, looking for new one...")

        # for the second iteration and on, thats the scroll amount
        scroll_amount= 72 * 24

    return addedContacts, removedContacts, errors, equalNames
