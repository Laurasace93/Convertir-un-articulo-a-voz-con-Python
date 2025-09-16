#Importamos librerias necesarias

from bs4 import BeautifulSoup #para parsear el HTML
from gtts import gTTS #para convertir texto a voz
import playsound #para reproducir el audio
import requests #para hacer solicitudes HTTP

#Obtener el texto del articulo
url = input("Ingresa la URL del articulo: ")
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    #Eliminar elementos no deseado
   
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()
        
    #Obtener el texto de los parrafos (p) del articulo
    text_elements = soup.find_all('p')
    article_text = ' '.join([p.get_text() for p in text_elements])
except requests.exceptions.RequestException as e:
    print(f"Error al obtener el articulo: {e}")   
    
#Convertir texto a voz con gTTS
tts = gTTS(text=article_text, lang='es')

#Guardar el archivo de audio
audio_file = "articulo.mp3"
tts.save(audio_file)

#Reproducir el archivo de audio
playsound.playsound(audio_file)