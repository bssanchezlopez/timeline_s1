import streamlit as st

# Título de la aplicación
st.title("Timeline con Slider e Imágenes desde GitHub")

# Slider con 5 puntos
valor = st.slider("Selecciona un punto del timeline", 1, 5, 1)

# Diccionario que mapea valores del slider con URLs de imágenes en GitHub
imagenes = {
    1: "https://raw.githubusercontent.com/usuario/repositorio/main/timeline_images/imagen1.png",
    2: "https://raw.githubusercontent.com/usuario/repositorio/main/timeline_images/imagen2.png",
    3: "https://raw.githubusercontent.com/usuario/repositorio/main/timeline_images/imagen3.png",
    4: "https://raw.githubusercontent.com/usuario/repositorio/main/timeline_images/imagen4.png",
    5: "https://raw.githubusercontent.com/usuario/repositorio/main/timeline_images/imagen5.png",
}

# Mostrar la imagen correspondiente al valor del slider
st.image(imagenes[valor], use_column_width=True)
