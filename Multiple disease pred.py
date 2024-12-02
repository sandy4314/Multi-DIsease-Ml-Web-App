# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 00:43:04 2024

@author: sande
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

diabetes_model=pickle.load(open("C:/Users/sande/OneDrive/Desktop/Multi Disease/saved models/diabetes_model.sav","rb"))

heart_model=pickle.load(open("C:/Users/sande/OneDrive/Desktop/Multi Disease/saved models/heart_model.sav","rb"))

kidney_model=pickle.load(open("C:/Users/sande/OneDrive/Desktop/Multi Disease/saved models/kidney_model.sav","rb"))

parkinsons_model=pickle.load(open("C:/Users/sande/OneDrive/Desktop/Multi Disease/saved models/parkinsons_model.sav","rb"))

with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction Sysrem',
                         ['Diabetes Prediction','Heart Disease Prediction','Kidney Disease Prediction','Parkinsons Prediction'],
                         icons=['activity','heart','capsule','person'],
                         default_index=0)
    
 

if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input("No.of Pregnancies")
    with col2:
        Glucose=st.text_input("Enter Glucose value")
    with col3:
        BloodPressure=st.text_input("Enter BloodPressure value")
    with col1:
        SkinThickness=st.text_input("Enter SkinThickness value")
    with col2:
        Insulin=st.text_input("Enter Insulin value")
    with col3:
        BMI=st.text_input("Enter BMI value")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Enter DiabetesPedigreeFunction value")
    with col2:
        Age=st.text_input("Enter Age of Person")
        
    diabetes_res=''
    
    if st.button('Diabetes Test Result'):
        
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        
        user_input=[float(i) for i in user_input]
        
        diabetes_pred=diabetes_model.predict([user_input])
    
        if(diabetes_pred[0]==1):
            diabetes_res='The Person Is Diabetic'
        
        else:
            diabetes_res='The Person Is Not Diabetic'
        
    
    st.success(diabetes_res)
    
        
    
if selected=='Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
       thal = st.selectbox(
            'Thal: Choose a condition',
            ['Normal (0)', 'Fixed Defect (1)', 'Reversible Defect (2)']
        )
    thal_mapping = {
    'Normal (0)': 0,
    'Fixed Defect (1)': 1,
    'Reversible Defect (2)': 2
}
 
    thal_value = thal_mapping[thal]
    
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal_value]

        user_input = [float(x) for x in user_input]

        heart_pred = heart_model.predict([user_input])

        if heart_pred[0] == 1:
            heart_diagnosis = 'The person is suffering with heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    


    
if selected == 'Kidney Disease Prediction':
    st.title('Kidney Disease Prediction Using ML')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        age = st.text_input("Age")
    with col2:
        bp = st.text_input("Blood Pressure")
    with col3:
        al = st.text_input("Albumin Value")
    with col4:
        su = st.text_input("Sugar Value")
    
    with col1:
        rbc = st.selectbox('Red Blood Cells', ['Normal', 'Abnormal'])
    with col2:
        pc = st.selectbox('Pus Cells (White Blood Cells)', ['Normal', 'Abnormal'])
    with col3:
        pcc = st.selectbox('Pus Cell Clumps', ['Present', 'NotPresent'])
    with col4:
        ba = st.selectbox('Bacteria', ['Present', 'NotPresent'])
    with col1:
        bgr = st.text_input('Random Blood Sugar Level (mg/dL)')
    with col2:
        bu = st.text_input('Blood Urea')
    with col3:
        sc = st.text_input('Serum Creatine (mg/dL)')
    with col4:
        pot = st.text_input('Potassium (mmol/L)')
    with col1:
        wc = st.text_input('White Blood Cell Count')
    with col2:
        htn = st.selectbox('Hypertension', ['Yes', 'No'])
    with col3:
        dm = st.selectbox('Diabetes Mellitus', ['Yes', 'No'])
    with col4:
        cad = st.selectbox('Coronary Artery Disease', ['Yes', 'No'])
    with col1:
        pe = st.selectbox('Pedal Edema', ['Yes', 'No'])
    with col2:
        ane = st.selectbox('Anemia', ['Yes', 'No'])
    
    # Mapping inputs
    rbc_mapping = {'Abnormal': 1, 'Normal': 0}
    pc_mapping = {'Abnormal': 1, 'Normal': 0}
    pcc_mapping = {'Present': 1, 'NotPresent': 0}
    ba_mapping = {'Present': 1, 'NotPresent': 0}
    binary_mapping = {'Yes': 1, 'No': 0}
    
    rbc = rbc_mapping[rbc]
    pc = pc_mapping[pc]
    pcc = pcc_mapping[pcc]
    ba = ba_mapping[ba]
    htn = binary_mapping[htn]
    dm = binary_mapping[dm]
    cad = binary_mapping[cad]
    pe = binary_mapping[pe]
    ane = binary_mapping[ane]
    
    kidney_res = ''
    
    if st.button('Kidney disease Test Result'):
        try:
            user_input = [age, bp, al, su, bgr, bu, sc, pot, wc]
            user_input = [float(i) if i else 0.0 for i in user_input]
            user_input.extend([rbc, pc, pcc, ba, htn, dm, cad, pe, ane])
            
            if 'kidney_model' not in globals():
                st.error("Model not loaded. Please ensure the model is available.")
                st.stop()
            
            kidney_disease_pred = kidney_model.predict([user_input])
            
            if kidney_disease_pred[0] == 1:
                kidney_res = 'Person is suffering with kidney disease'
            else:
                kidney_res = 'Person does not have kidney disease'
        except Exception as e:
            st.error(f"Error during prediction: {e}")
    
    st.success(kidney_res)

        
        





    
if selected=='Parkinsons Prediction':
    st.title('Parkinsons Prediction Using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    