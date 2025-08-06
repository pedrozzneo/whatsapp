import time
import driver as d
import utils
import list

# Set chrome driver and open whatsapp
driver = d.set()
driver.get("https://web.whatsapp.com")

# Filter "lista" contacts until it's successfull
success = False
time.sleep(500)
while not success:
    try:
        utils.search("fibra", driver)
        success = True
        time.sleep(10)
    except:
        continue

# Build all the lists
addedContacts, removedContacts, errors, equalNames= list.build(driver)

# Print them
utils.show(addedContacts, removedContacts, errors, equalNames)

time.sleep(5)

# Check if the user wants to start with a specific contact
while True:
    answer = input("\nGostaria de começar por algum contato específico? (sim/nao): ")
    if answer.lower() == "sim":
        addedContacts = list.filter(addedContacts)
        utils.show(addedContacts, removedContacts, errors, equalNames)
        break
    elif answer.lower() == "nao" or answer.lower() == "não":
        break
    else:
        print("Resposta inválida. Por favor, digite 'sim' ou 'nao' \n")

# Make sure the user is ready to use the program by coping the picture that will be used in the transmission list
while True:
    imageCopied = input("Copie a imagem para usar na lista de transmissão, digite \"sim\" quando copiar: ")
    if(imageCopied.lower() == "sim"):
        break
    else:
        print("Resposta inválida. Por favor, digite \"sim\" quando copiar \n")

# Message each contact
list.message(driver, addedContacts)  
