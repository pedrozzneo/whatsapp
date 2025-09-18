from selenium.webdriver.common.by import By
import utils
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def filter(addedContacts, profile):
    if profile == "thiago":
        filter = "Jana Clínica Giselle Oliveira Fibra Otica" 
    elif profile == "pedro":
        filter = "Charles Esteves Fibra Otica"
    elif profile == "flavia":
        filter = "Amanda Machado Fibra Otica" 
    
    # Make sure the filter exists in the list
    while True:
        if filter not in addedContacts:
            filter = input(f"{filter} não encontrado na lista de contatos, insira novamente: ")
        else:
            break
    
    # if filter in addedContacts:
    #     return addedContacts[addedContacts.index(filter)]
    
    # Actually filter the list
    while True:
        contact = addedContacts.pop(0)
        if contact == filter:
            addedContacts.append(contact)
            return addedContacts

def message(driver, addedContacts, profile):
    i = 0
    while addedContacts != [] and i < 200:
        time.sleep(12)
        try:
            # Get the first contact in the list
            contact = addedContacts.pop(0)

            # Search for the contact
            utils.search(contact, driver)
            time.sleep(10)

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
            time.sleep(11)

            # Make the input field empty
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

            # Copy the image
            utils.imageToClipboard(fr"C:\Users\nikao\Documents\Code\fibras\Images\{profile}")

            # Select a picture on the chat
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

            time.sleep(7)

            #Click the send button in PT
            try:
                send_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Enviar']"))
                )
            except:
                # Click the send button in EN
                send_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Send"]'))
                )

            send_button.click()
            time.sleep(8)

            #Type the message in the input field
            # message = "Bom dia!! Tudo bem? Estamos com condições especiais nas fibras, gostaria de saber mais?"
            # ActionChains(driver).send_keys(message).perform()

            # Send the message
            # ActionChains(driver).send_keys(Keys.RETURN).perform()
            
            # Save and output progress
            i += 1
            print(f"Mensagem para {contact} - {i} bem sucedida, {len(addedContacts)} restantes")
        except:
            # Log the error
            print(f"❌ Erro ao enviar mensagem para {contact}")

            # Re-add the contact to the list for retry
            addedContacts.append(contact) 
            continue

def build(driver):
    addedContacts = []
    removedContacts = []
    errors = []
    equalNames = []
    groupCount = 0
    validGroup = None

    # variable that determines the end of the loop
    end = False
    #or addedContacts.length <= 200
    while not end:
        time.sleep(3)
        # Find the group of contacts
        try:
            # log
            groupCount += 1
            print(f"\ncollecting contacts from group {groupCount} ... \n")

            # The list is loaded through groups
            group = WebDriverWait(driver, 30).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='x10l6tqk xh8yej3 x1g42fcv']"))
            )
            contactsAmount = len(group)
            print(f"contacts in this group: {contactsAmount}")

            distance = group[1].location['y']  - group[0].location['y']
        except Exception as e:
            print(f" ❌ unable to find a group of contacts {str(e)}")
            errors.append("unable to find a group of contacts")
        
        # Transfer the names of the group to the array
        for i in range(contactsAmount):
            try:
                # Extract the name of the contact
                name = group[i].text.split('\n')[0].strip()

                # Extract the location of the contact
                location = group[i].location['y']
            except:
                print("❌ unable to interact with contact")
                errors.append("unable to interact with contact")
                validGroup = False
                break

            # Means I reached the last contact of the group successfuly
            if i == (contactsAmount - 1):
                validGroup = True

            # Check for stop condition
            if name.lower() == "messages" or name.lower() == "mensagens":
                # Signalize the end of the loop
                end = True
                print("MESSAGES found, stop looking for other contacts")
                break

            # Check if the contact should not be added
            if "excluir" in name.lower() or "mec med" in name.lower() or name.lower() == "contacts" or name.lower() == "chats" or name.lower() == "conversas" or "fibra" not in name.lower() or "mec med" in name.lower():
                # Show the contact that will be skipped
                print(f"{i} - skipping contact: {name}")

                # Add the contact to the removed contacts array for further check
                removedContacts.append(name)
                continue
        
            # Add the contact to the array only if its new
            if name not in addedContacts:
                addedContacts.append(name)    
                print(f" {i} - {name} added at {location}")
            else:
                equalNames.append(name)
                print(f" {i} - {name} already on list at {location}")

        # Try again cause the group didnt work
        if validGroup == False:
            groupCount -= 1
            continue


        # REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT REMOVE THAT THAT REMOVE THAT THAT REMOVE THAT THAT REMOVE THAT THAT REMOVE THAT THAT REMOVE THAT THAT REMOVE THAT 
        # end = True

        # Quit the loop
        if end:
            print("End of contacts reached.")
            break

        # Scroll down to the next group of contacts
        if groupCount == 1:
            scroll_amount = distance * (contactsAmount + 7)
        else:
            scroll_amount = distance * (contactsAmount) 
        utils.scroll_inside_div_js(driver, scroll_amount)

        # Wait for the DOM to make this instance stale, giving room for the new one
        WebDriverWait(driver, 30).until(EC.staleness_of(group[0]))
        print("Old group become stale, looking for new one...")

    print("returning")
    return addedContacts, removedContacts, errors, equalNames
