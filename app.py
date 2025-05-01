import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="SE-RRHH • Selección de Personal",
    page_icon="👩‍💻",
    layout="centered"
)

# Definición de vacantes y sus condiciones
def get_vacantes():
    return [
        {
            "vacante": "Analista de Datos",
            "condicion": lambda r: r.get("interpretacion") == "sí" and r.get("sql") == "sí" 
            and r.get("ingles") in ["intermedio", "avanzado"]
        },
        {
            "vacante": "Asistente Administrativo",
            "condicion": lambda r: r.get("organizacion") == "sí" and r.get("ofimatica") == "sí"
            and r.get("atencion") == "sí" and r.get("ingles") in ["intermedio", "avanzado"]
        },
        {
            "vacante": "Técnico en Soporte",
            "condicion": lambda r: r.get("hardware") == "sí" and r.get("sistemas") == "sí" 
            and r.get("turnos") == "sí" and r.get("atencion") == "sí"
            and r.get("ingles") in ["básico", "intermedio", "avanzado"]
        }
    ]

# Función de evaluación: identifica vacantes que cumplen
def evaluar_candidato(respuestas):
    matches = [v["vacante"] for v in get_vacantes() if v["condicion"](respuestas)]

    if len(matches) == 1:
        if respuestas.get("disponibilidad") == "sí":
            return f"✅ Perfil coincide con vacante de: {matches[0]}"
        else:
            return f"🗓️ Agendar perfil valioso para: {matches[0]}, contactar luego si no se cubre la vacante"
    
    elif len(matches) > 1:
        if respuestas.get("disponibilidad") == "sí":
            return f"⚠️ Cumple requisitos para varias vacantes: {', '.join(matches)}. Solicitar preferencia."
        else:
            return f"🗓️ Perfil coincide con varias vacantes ({', '.join(matches)}), pero no disponible ahora. Agendar para contactar luego."
    
    else:
        return "❌ Ninguna vacante coincide. Considerar formación o revisar perfil."

# Interfaz Streamlit agrupada por tipo de habilidad
st.title("👩‍💻, Sistema Experto de Selección de Personal")

with st.form("form_habilidades"):
    respuestas = {}
    
    st.header("Áreas de experiencia")
    respuestas["organizacion"] = st.selectbox("¿En organización de agenda para coordinar múltiples tareas?", ["", "sí", "no"])
    respuestas["atencion"] = st.selectbox("¿En atención al cliente?", ["", "sí", "no"])
    respuestas["hardware"] = st.selectbox("¿En reparación y/o instalación de hardware?", ["", "sí", "no"])
    respuestas["interpretacion"] = st.selectbox("¿En interpretación de informes estadísticos o financieros para tomar decisiones?", ["", "sí", "no"])

    st.header("Habilidades Técnicas")
    respuestas["ofimatica"] = st.selectbox("¿Domina herramientas ofimáticas (Excel, Word)?", ["", "sí", "no"])
    respuestas["sistemas"] = st.selectbox("¿Conoce sistemas operativos?", ["", "sí", "no"])
    respuestas["sql"] = st.selectbox("¿Conoce SQL?", ["", "sí", "no"])

    st.header("Horario y Disponibilidad")
    respuestas["turnos"] = st.selectbox("¿Dispuesto a trabajar por turnos?", ["", "sí", "no"])
    respuestas["disponibilidad"] = st.selectbox("¿Disponibilidad inmediata?", ["", "sí", "no"])
    
    st.header("Manejo de Idiomas")
    respuestas["ingles"] = st.selectbox("Nivel de inglés", ["", "básico", "intermedio", "avanzado"])
    
    submit = st.form_submit_button("Evaluar candidato")

if submit:
    # Validar campos vacíos
    faltantes = [k for k, v in respuestas.items() if v == ""]
    if faltantes:
        st.error(f"Completa todas las preguntas antes de evaluar. Faltan: {', '.join(faltantes)}")
    else:
        resultado = evaluar_candidato(respuestas)
        if "❌" in resultado:
            st.error(resultado)
        elif "⚠️" in resultado:
            st.warning(resultado)
        else:
            st.success(resultado)

