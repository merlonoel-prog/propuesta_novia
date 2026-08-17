import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Una pregunta importante...", page_icon="❤️", layout="centered")

# Inicializar el estado
if "acepto" not in st.session_state:
    st.session_state.acepto = False

# --- PANTALLA PRINCIPAL ---
if not st.session_state.acepto:
    st.title("¿Quieres ser mi novia? ❤️")
    st.write("Tengo una pregunta muy importante para ti... Piensa bien tu respuesta 👇")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("¡SÍ! 🥰", use_container_width=True):
            st.session_state.acepto = True
            st.rerun()
            
    with col2:
        if st.button("No 😢", use_container_width=True):
            st.error("¡Ups! Parece que el botón 'No' está roto... Intenta con el otro 🙈")

# --- PANTALLA DE CELEBRACIÓN ---
else:
    st.balloons() # Lanza globos reales por toda la pantalla
    st.success("¡SABÍA QUE DIRÍAS QUE SÍ! 💖🎉")
    st.title("¡Te amo! ❤️🥰")
    st.image("https://giphy.com", caption="¡Eres lo mejor!")
