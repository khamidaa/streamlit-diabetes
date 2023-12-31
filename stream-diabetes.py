import pickle 
import streamlit as st 

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#judul web
st.title('Prediksi Diabetes')

#membagi kolom
col1,col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('Pregnancies')

with col2 :
    Glucose = st.text_input ('Glucose')

with col1 :
    BloodPressure = st.text_input ('Blood Pressure')

with col2 :
    SkinThickness = st.text_input ('Skin Thickness')

with col1 : 
    Insulin = st.text_input ('Insulin')

with col2 :
    BMI = st.text_input (' BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input (' Diabetes Pedigree Function')

with col2 :
    Age = st.text_input ('Age')

#code untuk prediksi
diab_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
     diab_prediction = diabetes_model.predict([[Pregnancies, Glucose,BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ]])

     if(diab_prediction[0] == 1):
          diab_diagnosis = 'Prediksi Terkena Diabetes'
     else :
          diab_diagnosis = 'Pasien Tidak terkena Diabetes'

st.success(diab_diagnosis)