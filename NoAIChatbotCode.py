#CHATBOT SIN IA Programa realizado por TofuDev (José Alberto Ávila Pérez)
!pip install pycloudflared streamlit
#Instalamos primero OpenAI (resulta que dipsik viene aquí)
!pip install -q openai
from pycloudflared import try_cloudflare
tunnel = try_cloudflare(port=8501)
print(f"Haz clic aquí para ver tu app: {tunnel.tunnel}")
!streamlit run SimpleChat.py --server.port 8501

##App de Streamlit
%%writefile SimpleChat.py
import streamlit as st

st.set_page_config (
    page_title = 'Chatbot Tutor de Programación',
    page_icon = '👽',
)

st.title("👽💻 Chatbot Tutor de Programación")
st.image("https://media.tenor.com/HAnDm32K3L0AAAAi/alien.gif")

# Función que analiza el texto y responde según nuestro diccionario de palabras clave
def genera_respuesta(texto_usuario):
    # Convertiremos a minúsculas para que sea más fácil buscar las palabras que puedan usar
    texto = texto_usuario.lower()

    ## Cambié mi primer acercamiento (un montón de elifs) por un diccionario, así podré actualizar de forma más efectiva.
    respuestas = {
        ("secuencia", "orden", "pasos"):  "¡Claro! 📚 La **secuenciación** es la estructura más básica en programación. Significa que las instrucciones se ejecutan una tras otra, exactamente en el orden en que fueron escritas. ⬇️ Paso 1, luego Paso 2, luego Paso 3...",
        ("iteracion" ,"iteración" ,"ciclo" ,"bucle" , "for" ,"while"): "¡Las repeticiones son geniales! 🔁 La **iteración** o ciclos como los `for` o `while` permiten ejecutar un bloque de código varias veces hasta que se cumpla una condición. ¡Te ahorra escribir el mismo código muchas veces!",
        ("seleccion", "selección", "condicion", "condición", "condicional" , "if"): "¡Excelente pregunta! 🤔 La **selección**, o condicional, permite que tu programa tome decisiones. En Python usamos palabras como `if`, `else` o `elif` para ejecutar un bloque de código SOLO si se cumple una condición específica. 🛤️",
        ("hola", "saludos", "buenos días"): "¡Hola! 👽👋 Soy tu tutor virtual de programación. Puedo ayudarte a **entender** conceptos básicos como **secuenciación**, **selección** o **iteración**. ¿Sobre qué tema te gustaría aprender hoy?",
        ("adios" ,"chao", "hasta luego"): "Nos vemos, espero haberte ayudado, no olvides limpiar el chat y suerte con tus temas de programación"
        #Añadimos una opción de despedida (no hay que despedirnos de LLM's pero xd hay que poner la opción)
        }
    #Una vez definimos el diccionario, podemos ya buscar las palabras clave y las enlazamos con su respuesta.

    for palabras_clave, respuesta in respuestas.items():
        # Si alguna de las palabras clave está en el texto del usuario, regresa esa respuesta
        if any(palabra in texto for palabra in palabras_clave):
            return respuesta
    # Respuesta por defecto si no detecta palabras clave
    return "Mmm, no estoy seguro de entender. 💀 Como un pequeño tutor de programación, estoy especializado en  explicar cómo funcionan algunos temas como **secuenciación**, **selección** e **iteración**. ¿Podrías preguntarme utilizando alguna de esas palabras? 💻"

# Inicializar la historia del chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy tu tutor de programación 👽. Pregúntame sobre secuenciación, selección o iteración."}
    ]

# Mostrar la historia de los mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Reacción a la entrada del usuario
if prompt := st.chat_input("Escribe tu pregunta sobre programación aquí..."):
    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta basada en el prompt del usuario
    respuesta = genera_respuesta(prompt)

    # Guardar y mostrar respuesta del bot
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
    with st.chat_message("assistant"):
        st.markdown(respuesta)

# Botón para limpiar el chat
if st.button("🧹 Limpiar chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy tu tutor de programación 🤖. Pregúntame sobre secuenciación, selección o iteración."}
    ]
    st.rerun() # Recarga la app para limpiar la pantalla