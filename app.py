import streamlit as st

if "acepto" not in st.session_state:
    st.session_state.acepto = False

# Coloca aquí tu número de teléfono con el código de país (sin el signo + ni espacios)
# Ejemplo para Nicaragua: "50558444095"
NUMERO_TELEFONO = "50558444095" 

# --- PANTALLA PRINCIPAL ---
if not st.session_state.acepto:
    st.title("¿Quieres ser mi novia? 💕")
    st.write("Tengo una pregunta muy importante para ti... Piensa bien tu respuesta:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("¡SÍ! 🥳", use_container_width=True):
            st.session_state.acepto = True
            st.rerun()

    with col2:
        if st.button("No 😡", use_container_width=True):
            st.error("¡Ups! Parece que el botón 'No' está roto... Intenta con la otra opción. 😉")

# --- PANTALLA DE CELEBRACIÓN ---
else:
    st.balloons()
    st.success("¡SABÍA QUE DIRÍAS QUE SÍ! 💕🎉")
    st.title("¡Te amo! 💞")
    
    # Esta forma es más sencilla y siempre funciona
    url_whatsapp = "https://wa.me/50500000000?text=¡Dije+que+SÍ!+❤️🥰"
    st.link_button("📲 Enviarme confirmación por WhatsApp", url_whatsapp)
    
    mensaje = "¡Dije que SÍ! ❤️🥰"
    url_whatsapp = f"https://wa.me/{NUMERO_TELEFONO}?text={mensaje}"
    
    st.markdown(
        f'<a href="{url_whatsapp}" target="_blank" style="display: inline-block; padding: 12px 24px; background-color: #25D366; color: white; text-align: center; font-weight: bold; border-radius: 8px; text-decoration: none; font-size: 18px;">📲 Enviarme confirmación por WhatsApp</a>',
        unsafe_allow_html=True
    )
