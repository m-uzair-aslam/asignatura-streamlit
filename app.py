from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Asignatura", page_icon="📡", layout="wide")

BASE = Path(__file__).parent

SECCIONES = {
    "Inicio": None,
    "Apuntes": "apuntes",
    "Ejercicios": "ejercicios",
    "Código": "codigo",
}

st.sidebar.title("📡 Mi asignatura")
seccion = st.sidebar.radio("Sección", list(SECCIONES.keys()))

if seccion == "Inicio":
    st.title("Bienvenido a la asignatura")
    st.write("Usa el menú de la izquierda para acceder al material.")
else:
    st.title(seccion)
    carpeta = BASE / SECCIONES[seccion]
    ficheros = sorted(p for p in carpeta.glob("*") if p.is_file())

    if not ficheros:
        st.info("Todavía no hay material en esta sección.")

    for f in ficheros:
        with st.expander(f.name):
            if f.suffix == ".py":
                st.code(f.read_text(encoding="utf-8"), language="python")
            st.download_button(
                label="Descargar",
                data=f.read_bytes(),
                file_name=f.name,
                key=str(f),
            )