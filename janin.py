import pickle
import streamlit as st

# membaca model
janin_model = pickle.load(open('janin_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Kesehatan Janin')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    baseline_value = st.number_input ('Detak Jantung Janin Dasar (FHR)')
    accelerations = st.number_input ('Peningkatan detak jantung janin')
    fetal_movement = st.number_input ('Jumlah gerakan janin per detik')
    uterine_contractions = st.number_input ('Jumlah kontraksi uterus per detik')
    light_decelerations = st.number_input ('Jumlah gerakan janin per detik', key='light_decelerations')
    

with col2 :
    severe_decelerations = st.number_input ('Penurunan detak jantung janin yang signifikan')
    prolongued_decelerations= st.number_input ('Penurunan detak jantung janin yang tiba-tiba dan berkelanjutan')
    abnormal_short_term_variability = st.number_input ('Pola variabilitas yang tidak wajar atau tidak normal dalam detak jantung janin selama periode pendek')
    mean_value_of_short_term_variability= st.number_input ('Nilai rata-rata dari variabilitas')
    percentage_of_time_with_abnormal_long_term_variability= st.number_input ('persentase waktu di mana variabilitas jangka panjang')

# code untuk prediksi
janin_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Janin'):
    janin_prediction = janin_model.predict([[baseline_value, accelerations, fetal_movement, uterine_contractions,
                                            light_decelerations, severe_decelerations,prolongued_decelerations, 
                                            abnormal_short_term_variability, mean_value_of_short_term_variability,
                                            percentage_of_time_with_abnormal_long_term_variability]])

    if janin_prediction == 3:
        janin_diagnosis = 'Kondisi janin tidak baik (Pathological)'
    elif janin_prediction == 2:
        janin_diagnosis = 'Kondisi janin tidak normal (Suspect)'
    else:
        janin_diagnosis = 'Kondisi janin sehat (Normal)'
st.success(janin_diagnosis)