import streamlit as st
import math

st.title("menghitung tabung :blue[volume tabung] :rocket:")

r = st.number_input("Masukan jari-jari (cm):",0)
t = st.number_input("Masukan tinggi (cm):",0)

if st.button("Hitung volume", type="primary"):
  v = math.pi*(r**2)*t
  st.succes(f"volume tabung adalah(v:.2f)")
