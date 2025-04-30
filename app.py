import streamlit as st

def evaluar_candidato(respuestas):
    reglas = [
        {
            "vacante": "Analista de Datos",
            "condiciones": lambda r: r["datos"] == "sí" and r["sql"] == "sí" and r["ingles"] in ["intermedio", "avanzado"] and r["disponibilidad"] == "inmediata"
        },
        {
            "vacante": "Asistente Administrativo",
            "condiciones": lambda r: r["organizacion"] == "sí" and r["ofimatica"] == "sí" and r["trata_clientes"] == "sí"
        },
        {
            "vacante": "Técnico en Soporte",
            "condiciones": lambda r: r["hardware"] == "sí" and r["sistemas"] == "sí" and r["turnos"] == "sí"
        }
    ]

    for regla in reglas:
        if regla["condiciones"](respuestas):
            return f"Candidato apto para la vacante: {regla['vacante']}"

    return "Ninguna vacante coincide completamente. Considere otras opciones."

st.title("🧠 Sistema Experto de Selección de Personal")

st.write("Responda las siguientes preguntas con **sí** o **no**, y seleccione el nivel de inglés.")

with st.form("formulario"):
    respuestas = {}
    respuestas["datos"] = st.selectbox("¿Tiene experiencia en análisis de datos?", ["sí", "no"])
    respuestas["sql"] = st.selectbox("¿Conoce SQL?", ["sí", "no"])
    respuestas["ingles"] = st.selectbox("Nivel de inglés", ["básico", "intermedio", "avanzado"])
    respuestas["disponibilidad"] = st.selectbox("¿Está disponible de forma inmediata?", ["sí", "no"])

    respuestas["organizacion"] = st.selectbox("¿Tiene habilidades de organización?", ["sí", "no"])
    respuestas["ofimatica"] = st.selectbox("¿Domina herramientas ofimáticas (Excel, Word)?", ["sí", "no"])
    respuestas["trata_clientes"] = st.selectbox("¿Tiene experiencia tratando con clientes?", ["sí", "no"])

    respuestas["hardware"] = st.selectbox("¿Tiene experiencia reparando hardware?", ["sí", "no"])
    respuestas["sistemas"] = st.selectbox("¿Tiene conocimientos de sistemas operativos?", ["sí", "no"])
    respuestas["turnos"] = st.selectbox("¿Está dispuesto a trabajar por turnos?", ["sí", "no"])

    submit = st.form_submit_button("Evaluar")

if submit:
    resultado = evaluar_candidato(respuestas)
    st.success(resultado)

