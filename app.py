import streamlit as st

# Título de la aplicación
st.title("Detección de transacciones fraudulentas | Timeline")
st.write("Autor: Brenda Sánchez López | BCP")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de las transacciones fraudulentas.")

# Diccionario que mapea valores del slider con URLs de imágenes en GitHub
imagenes = {
    1: "https://raw.githubusercontent.com/bssanchezlopez/timeline_s1/main/timeline_images/timeline1.png",
    2: "https://raw.githubusercontent.com/bssanchezlopez/timeline_s1/main/timeline_images/timeline2.png",
    3: "https://raw.githubusercontent.com/bssanchezlopez/timeline_s1/main/timeline_images/timeline3.png",
    4: "https://raw.githubusercontent.com/bssanchezlopez/timeline_s1/main/timeline_images/timeline4.png",
    5: "https://raw.githubusercontent.com/bssanchezlopez/timeline_s1/main/timeline_images/timeline5.png",
}

# Slider
opcion = st.slider(
"Selecciona un punto del timeline",
min_value=1,
max_value=5,
value=1,
step=1
)

# Mostrar imagen según slider
st.image(imagenes[opcion], use_container_width=True)
if opcion == 1:
st.info("**Década de 1950–60:** Aparición de los primeros sistemas manuales de revisión de transacciones con tarjetas de crédito.")
if opcion == 2:
st.info("**Década de 1980:** Introducción de sistemas basados en reglas (“rule-based systems”) para identificar comportamientos sospechosos.")
if opcion == 3:
st.info("**Década de 1990:** Uso inicial de modelos estadísticos y scoring para evaluar riesgo de fraude.")
if opcion == 4:
st.info("**Década de 2000:** Adopción masiva del machine learning para detectar patrones complejos en grandes volúmenes de datos.")
if opcion == 5:
st.info("**Década de 2010–actualidad:** Integración de IA avanzada, análisis en tiempo real y biometría para prevenir fraudes de manera predictiva.")
