import time
import driver as d
import utils
import list
import os

# Make sure the user is ready to use the program by coping the picture that will be used in the transmission list
while True:
    imageCopied = input("COPIE A IMAGEM QUE VOCE GOSTARIA DE UTILIZAR NA LISTA DE TRANSMISSAO, DIGITE \"sim\" QUANDO COPIAR: ")
    if(imageCopied.lower() == "sim"):
        break
    else:
        print("NAO ENTENDI, POR FAVOR DIGITE \"sim\" QUANDO COPIAR")

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
addedContacts, removedContacts, errors, equalNames= list.build(driver)

# Print them
utils.show(addedContacts, removedContacts, errors, equalNames)

answer = input("wanna start from a specific contact? ")
if answer == "y":
    contact = input("enter the exact name of the contact: ")
    addedContacts = list.filter(addedContacts, contact)
    # Print them
    utils.show(addedContacts, removedContacts, errors, equalNames)

# Message each contact
list.message(driver, addedContacts)  
