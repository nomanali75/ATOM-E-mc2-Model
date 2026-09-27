import streamlit as st

st.set_page_config(page_title="ATOM E=mc2 Model", page_icon="⚛️")

st.title("⚛️ ATOM E=mc² Model")
st.subheader("Qazi 1st Ground Law: E = m · Gf")
st.caption("By Noman Ali Qazi | CERN DOI: 10.5281/zenodo.23000987 | 26/9/26")
st.divider()

st.markdown("**Conceptual model interpreting E=mc² via structured atomic binding**")

m = st.number_input("Mass (m) in kg", value=1.0)
Gf = st.number_input("Ground Force (Gf)", value=9.81)
E = m * Gf

st.metric("Energy E = m·Gf", f"{E} Joules")
st.success(f"E = {m} × {Gf} = {E}")
st.divider()
st.write("ATOM Analogy Model - Noman Ali Qazi")
