import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('**EMPLEATRONIX**')

st.write('Todos los datos sobre los empleados en una aplicación.')

df = pd.read_csv("data/employees.csv")
nombres = df["full name"]
sueldos = df["salary"]
st.dataframe(df, width=600, height=400)

st.divider()

c1, c2, c3 = st.columns(3)
color = c1.color_picker("Elige un color para las barras", "#0A497B")
t_nombre = c2.toggle("Mostrar el nombre")
t_sueldo = c3.toggle("Mostrar sueldo en la barra")

fig, ax = plt.subplots()
barras = ax.barh(nombres, sueldos, color=color)

if not t_nombre:
    plt.yticks([])
    
ax.set_title('Gráfico de Barras Horizontales')

if t_sueldo:
    for barra in barras:
        sueldo = barra.get_width()
        ax.text(barra.get_width(), barra.get_y() + barra.get_height() / 2, f"{sueldo}€", va='center')

ax.set_xlim([0, 4300])
st.pyplot(fig)

st.markdown("© Pablo Martín Trujillo - CPIFP Alan Turing")
