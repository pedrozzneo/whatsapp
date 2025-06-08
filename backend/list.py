from selenium.webdriver.common.by import By
import utils
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def message(driver, addedContacts):
    for i, contact in enumerate(addedContacts, start=1):
        try:
            utils.clear_search_field(driver)
            utils.search(contact, driver)
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, f"(//div[@class='x10l6tqk xh8yej3 x1g42fcv'])[{2}]"))
            )
            element.click()
            
            ActionChains(driver).send_keys(Keys.BACKSPACE * 120).perform()

            message = "Bom dia!! Tudo bem? Estamos com condições especiais nas fibras, gostaria de saber mais?"
            ActionChains(driver).send_keys(message).perform()

            print(f"message contact {contact} ({i}/{len(addedContacts)})")
        except Exception as e:
            print(f"Error messaging contact {contact}: {str(e)}")
            continue

def show(addedContacts, removedContacts, errors):
    # Show the added contacts collected
    print(f"\n list of contacts added: \n")
    for i, contact in enumerate(addedContacts, start=1):
        print(f"{i}: {contact}")

    # Show the deleted collected 
    print(f"\n list of contacts removed: \n")
    for i, contact in enumerate(removedContacts, start=1):
        print(f"{i}: {contact}")

    # Show the errors collected
    if errors:
        print(f"\n list of errors: \n")
        for error in errors:
            print(error)
    else:
        print("\n No errors found.")

def build(driver):
    addedContacts = []
    removedContacts = []
    errors = []

    # variable that determines the end of the loop
    end = False

    # The scroll amount only for the first iteration
    scroll_amount= 72 * 27 

    # Scrolls to fit perfectly the "lista" contacts
    utils.scroll_inside_div_js(driver, 243)

    while not end:
        # The list is loaded each 25 itens because of page size
        for i in range(1, 25):
            try:
                # Find the WebElement reference of the contact
                element = driver.find_element(By.XPATH, f"(//div[@class='x10l6tqk xh8yej3 x1g42fcv'])[{i}]")
                
                # Extract its name
                name = element.text.split('\n')[0].strip()
                
                # Check for stop condition
                if name == "MESSAGES":
                    # Signalize the end of the loop
                    end = True
                    break

                # Check if the contact should not be added
                if "excluir" in name.lower() or name == "CONTACTS":
                    # Show the contact that will be skipped
                    print(f"skipping contact: {name}")

                    # Add the contact to the removed contacts array for further check
                    removedContacts.append(name)
                    continue
                
                # Output the contact that will be added
                print(f"adding contact: {name}")

                # Add the contact to the array only if its new
                if name not in addedContacts:
                    addedContacts.append(name)     

            except Exception as e:
                print(f"error {e}")
                errors.append(f"error {str(e)}")

        # Quit the loop
        if end:
            print("End of contacts reached.")
            break

        # Get ready for the next iteration
        utils.scroll_inside_div_js(driver, scroll_amount)
        
        # for the second iteration and on, thats the scroll amount
        scroll_amount= 72 * 24

    # Remove the first element which is "CHATS"
    addedContacts.pop(0) 
    return addedContacts, removedContacts, errors
