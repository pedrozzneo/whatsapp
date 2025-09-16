import time
import driver as d
import utils
import list
import time
from datetime import datetime

# Espera dar 07:00 para iniciar a aplicação
while True:
    agora = datetime.now()
    if agora.hour >= 7 and agora.hour <= 16:
        break
    time.sleep(60)  

# profile = "thiago"
# profile = "pedro"
profile = "flavia"

# Set chrome driver and open whatsapp
driver = d.set(profile)
driver.get("https://web.whatsapp.com")

time.sleep(100)

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

time.sleep(5)

# Start with a specific contact
addedContacts = list.filter(addedContacts, profile)
utils.show(addedContacts, removedContacts, errors, equalNames)
       
# Make sure the user is ready to use the program by coping the picture that will be used in the transmission list
# while True:
#     imageCopied = input("Copie a imagem para usar na lista de transmissão, digite \"sim\" quando copiar: ")
#     if(imageCopied.lower() == "sim"):
#         break
#     else:
#         print("Resposta inválida. Por favor, digite \"sim\" quando copiar \n")

# Message each contact
list.message(driver, addedContacts)  
