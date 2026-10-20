import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="Mon SaaS IA", page_icon="⚡", layout="centered")

st.title("⚡ Mon SaaS de Génération de Contenu")
st.write("Bienvenue ! Générez vos textes en un clic grâce à l'IA.")

# Gestion de la clé d'API (ou intégration système)
api_key = st.text_input("Entrez votre clé API (ou laissez vide si configurée) :", type="password")

if api_key:
    genai.configure(api_key=api_key)

# Formulaire utilisateur
prompt = st.text_area("Saisissez votre sujet ou besoin :", placeholder="Ex: Rédige un post LinkedIn sur le marketing SaaS...")

button = st.button("🚀 Générer le contenu")

if button:
    if not prompt:
        st.warning("Veuillez entrer un sujet.")
    else:
        with st.spinner("Génération en cours..."):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                
                st.success("Terminé !")
                st.subheader("Résultat :")
                st.write(response.text)
            except Exception as e:
                st.error(f"Une erreur s'est produite : {e}")
