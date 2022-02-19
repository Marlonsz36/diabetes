# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import joblib 
import pandas as pd
import time
st.image("logo.png",use_column_width=True)

st.title("Detección temprana de diabetes")
st.caption("<font color=‘blue’>Advertencia, realizar esta prueba de deteccion temprana una vez se haga hecho pruebas de quimica sanguinea y prueba de orina</font>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input('Inserte su edad',min_value=18,max_value=90)
    BMI = st.number_input('Inserte su indice de masa corporal',min_value=15.00)
    #Renal= st.radio(
     #"Usted ha sufrido de falla renal?",
    # ('Si', 'No'))
    Lactate = st.number_input('Inserte su concentración de lactato',min_value=0.00)
    Calcium = st.number_input('Inserte su concentración de calcio',min_value=0.00)

with col2:
    etnic = st.selectbox(
         'Ingrese el grupo éntico al que pertenece',
         ('Caucásico', 'Nativo Americano','Africano Americano', 'Asiático', "Hispano", "Otros"))
    Glucose = st.number_input('Inserte su nivel de glucosa')
   # Respiratory = st.radio(
    # "Ha recibido recientemente ventilacion invasiva(intubacion)?",
    # ('Si', 'No'))
    Hemoglobin = st.number_input('Inserte su concentración de hemoglobina',min_value=0.00)
    Creatinine = st.number_input('Inserte su concentración de creatinina',min_value=0.00)


#def binario(sino):
 #       if(sino== "Si"):
  #          return 1
   #     elif(sino== "No"):
    #        return 0
        
        
def etnia(valor):
        if(valor=="Caucásico"):
            return "Caucasian"
        elif(valor=="Nativo Americano"):
            return "Native American"
        elif(valor=="Africano Americano"):
            return "African American"
        elif(valor=="Asiático"):
            return "Asian"
        elif(valor=="Hispano"):
            return "Hispanic"
        elif(valor=="Otros"):
            return "Other/Unknown"

def glycosilated(Glucosa):
    return round((Glucosa+46.7)/28.7,1)
modelo=joblib.load("diabetes.pkl")
#data={"glucose":30,"bmi":75,"arf":0,"age":45,"ventilated":0,"etnic":"Caucasican","hemaglobin":65,"glucosylated_hemaglobin":5.8,"lactate":50,"creatinine":50,"calcium":50}
df = pd.DataFrame(
    [[Glucose,BMI,0,Age,0,etnia(etnic),Hemoglobin,glycosilated(Glucose),Lactate,Creatinine,Calcium]],
    columns=("glucose", "bmi","arf","age","ventilated","ethnicity","d1_hemaglobin_max","glycosylated_hemoglobin","d1_lactate_max","creatinine","d1_calcium_max"))

#st.dataframe(df)  # Same as st.write(df)

if (st.button('Diagnosticar')):
    with st.spinner('Por Favor espere...'):
        time.sleep(7)
    diabetes=modelo.predict(df)
    if(diabetes==1):
        st.error("Desafortunadamente los resultados indican que puedes tener diabetes, te recomendamos que te realices exámenes más especializados para ver tu tratamiento")
    elif(diabetes==0):
        st.success("Los resultados indican que por el momento no corres riesgo de diabetes, pero te dejamos la siguiente información de prevención")
        st.image("infodiabetes.jpg",use_column_width=True)
