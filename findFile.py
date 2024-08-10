import os
import psutil
import sys
import ctypes
import docx
import PyPDF2
from odf.opendocument import load
from odf.text import P
import shutil

def run_as_admin():
    try:
        # Solicita permisos de administrador
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    except Exception as e:
        print(f"Error al solicitar permisos de administrador: {e}")
        sys.exit(1)

if ctypes.windll.shell32.IsUserAnAdmin():
    pass
else:
    run_as_admin()
    
    
    
#  -----------------------------------------------------------------------------

#  Functions to read files:

def readInOdt(file:str, word:str):
    doc = load(file)
    for parrafo in doc.getElementsByType(P):
        if word in str(parrafo).lower():
            return True
    return False

def readInWord(file:str, word:str):
    doc = docx.Document(file)
    for para in doc.paragraphs:
        if word in para.text.lower(): return True
    return False

def readInPdf(file:str, word:str):
    with open(file, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            if word in text.lower(): return True
        return False

def readInNotePad(file:str, word: str):
    with open(file, 'r', encoding='utf-8', errors ='ignore') as f:
        return word in f.read().lower()
    
#  -----------------------------------------------------------------------------


text2find = set([text.strip() for text in input("¿Qué quieres que busque en el contenido de los archivos?\n(para buscar varias palabras, separar con \",\")\n(Pulsar ENTER si no se quiere buscar en los contenidos):\n> ").lower().split(",")])
extensions = set([])
textInPath = set([])
patron = set([ p.strip() for p in input("""\nQué palabras debe contener la ruta y/o qué extensiones deben tener los archivos? (NO PONER ESPACIOS)
    EXTENSIONES SOPORTADAS:  *odt,*docx,*pdf,*rtf,*txt,*json,*csv,*excl,*ods,*aut,*db,*py,*bat,*log,*ini,*htm,*html,*xml,*cpp,*js
    Ejemplo de uso:  cisco,redes,net,*pdf,*odt,*any
    (*any significa que se buscará en cualquier archivo que se pueda abrir con el blog de notas)
> """).lower().split(",")])
for i in patron:
    if i.startswith("*") and i!= "*any": extensions.add(i[1::])
    elif i == "*any": extensions.update(set(["txt", "json", "csv", "ods", "xcl", "aut", "db", "py", "bat", "log", "ini", "htm", "html", "xml", "cpp", "js"]))
    else: textInPath.add(i)
    

directories = set([input("Desde dónde quieres que busque?:\n> ")+"\\"])

files = set()
if __name__ == '__main__':

    while directories:
        path = directories.pop()
        try:
            print(f'Intentando acceder a {path}')
            os.chdir(path)
            itemsInPath = os.listdir(path)
            for item in itemsInPath:
                itemPath = path+item
                if os.path.isdir(itemPath):
                    directories.add(itemPath+"\\")
                    continue

                if not (any(i in itemPath for i in textInPath) or textInPath==set() ) or not ( not "." in item or ( "." in item and any(i==item.split(".")[1] for i in extensions))):
                    continue
                try:

                    if "." in item and item.split(".")[1] in ["docx"]:
                        for element2find in text2find:
                            if readInWord(itemPath, element2find): files.add(itemPath)
                        
                    elif "." in item and item.split(".")[1] in ["pdf"]:
                        for element2find in text2find:
                            if readInPdf(itemPath, element2find): files.add(itemPath)
                                    
                    elif "." in item and item.split(".")[1] in ["odt"]:
                        for element2find in text2find:
                            if readInOdt(itemPath, element2find): files.add(itemPath)
                    else:
                        for element2find in text2find:
                            if readInNotePad(itemPath, element2find):
                                files.add(itemPath)
                            
                except Exception as error:
                    print("No se pudo abrir el archivo: ",error)
                    
        except Exception as e:
            print('Error:', e)


ruta_script = os.path.dirname(os.path.realpath(__file__))
newFolder = os.path.join(ruta_script, 'outputFiles')
if not os.path.exists(newFolder):
    os.makedirs(newFolder)
else:
    for filename in os.listdir(newFolder):
        file_path = os.path.join(newFolder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Error al borrar {file_path}. Razón: {e}')
            
print("Archivos que tengan:\n - Las palabras \"", end="")
print(*text2find, sep="\", \"", end="\" en su contenido\n - Cuya extensión es una de estas: ") 
print(*extensions, sep=', ', end="\n - Con las palabras \"")
print(*textInPath, sep="\", \"", end="\" en su ruta\n") 
for filePath in files:
    shutil.copy(filePath, newFolder)
    print(filePath)
print('Archivos guardados en:', newFolder)
