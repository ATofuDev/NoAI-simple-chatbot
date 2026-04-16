# 👽💻 Chatbot Tutor de Programación

Chatbot educativo desarrollado con Streamlit que ayuda a estudiantes a
entender los conceptos básicos de programación: secuenciación, selección
e iteración.

![Chatbot demo](https://media.tenor.com/HAnDm32K3L0AAAAi/alien.gif)

## 🛠️ Tecnologías usadas

- Python
- Streamlit
- pycloudflared (para tunneling y acceso público)

## ⚙️ Instalación

1. Clona el repositorio:
   git clone https://github.com/atofudev/...

2. Instala las dependencias:
   pip install streamlit pycloudflared

3. Corre la app:
   streamlit run SimpleChat.py

## 💬 ¿Cómo funciona?

El chatbot analiza el texto del usuario y lo compara contra un diccionario
de palabras clave. Dependiendo del término detectado (como "for", "if",
"ciclo", etc.), responde con una explicación del concepto correspondiente.

Temas que puede explicar:
- Secuenciación
- Selección / Condicionales (if, else, elif)
- Iteración / Ciclos (for, while)

## 🧠 Decisiones técnicas

Se optó por un diccionario de palabras clave en lugar de una cadena de
if/elif para facilitar el mantenimiento y la escalabilidad del bot.
Agregar un nuevo tema solo requiere añadir una entrada al diccionario.

## 🚀 Posibles mejoras

- Integrar un LLM (como la API de Deepseek) para respuestas más naturales
- Añadir más temas de programación
- Soporte multilenguaje (inglés/español)

## 👤 Autor

José Alberto Ávila Pérez — TofuDev
