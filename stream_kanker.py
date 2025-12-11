import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler
from streamlit_option_menu import option_menu

#navigasi sidebar
# judul web
st.title('Aplikasi Prediksi Kanker Payudara Ganas dan Jinak'
# horizontal menu
selected2 = option_menu(None, ["Data", "Preprocessing data", "Modelling", 'Implementasi'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")


#halaman Data
if (selected2 == 'Data') :
    st.title('deskripsi data')

    st.write("Ini adalah contoh data yang tersedia dalam aplikasi Streamlit")
    st.write("Data ini berisi 30 kolom untuk memprediksi Kanker ganas dan kanker jinak")
    st.write("Data ini diambil dari kaggle")
    st.write("Data ini merupakan type data Numerik")
    data = pd.read_csv('https://raw.githubusercontent.com/risma260/dataset_cancer/main/DATA_KANKER.csv', sep=';')
    st.write(data)



#halaman preprocessing data 
if (selected2 == 'Preprocessing data') :
    st.title('Preprocessing Data')

    st.write("Saya menggunakan Preprocessing Data MinMax Scaler ")
    data = pd.read_csv('preprocessed_kanker.csv')
    st.write(data)

#halaman modelling
if (selected2 == 'Modelling'):
    st.title('Modelling')

    pilih = st.radio('Pilih', ('Naive Bayes', 'Decision Tree', 'KNN', 'ANN'))

    if (pilih == 'Naive Bayes'):
        st.title(' Nilai Akurasi 0,92%')
    elif (pilih == 'Decision Tree'):
        st.title(' Nilai Akurasi 0,95%')
    elif (pilih == 'KNN'):
        st.title(' Nilai Akurasi 0,84%')
    elif (pilih == 'ANN'):
        st.title(' Nilai Akurasi 0,52%')
         
#halaman Implementasi
if (selected2 == 'Implementasi'):
    st.title('Implementasi')

    # membaca model
    kanker_model = pickle.load(open('Kanker_KNN.pkl', 'rb'))

    #membagi kolom
    col1, col2, col3 = st.columns(3)

    with col1:

        radius_mean = st.number_input('radius mean')

        texture_mean = st.number_input('texture mean')

        perimeter_mean = st.number_input('perimeter mean')

        area_mean = st.number_input('area mean')	

        smoothness_mean	= st.number_input('smoothness mean')

        compactness_mean = st.number_input('compactness mean')	

        concavity_mean = st.number_input('concavity mean')	

        concave_points_mean	= st.number_input('concave points mean')

        symmetry_mean = st.number_input('symmetry mean')

        fractal_dimension_mean = st.number_input('fractal dimension mean')
    
    with col2: 

        radius_se = st.number_input('radius se')	

        texture_se = st.number_input('texture se')	

        perimeter_se = st.number_input('perimeter se')	

        area_se	= st.number_input('area se')

        smoothness_se = st.number_input('smoothnessse')

        compactness_se = st.number_input('compactness se')	

        concavity_se = st.number_input('concavity se')	

        concave_points_se = st.number_input('concave_points se')	

        symmetry_se = st.number_input('symmetry se')	

        fractal_dimension_se = st.number_input('fractal dimension se')	

    with col3:
        radius_worst = st.number_input('radius worst')	

        texture_worst = st.number_input('texture worst')	

        perimeter_worst = st.number_input('perimeter worst')	

        area_worst = st.number_input('area worst')

        smoothness_worst = st.number_input('smoothness worst')	

        compactness_worst = st.number_input('compactness worst')	

        concavity_worst = st.number_input('concavity worst')	

        concave_points_worst = st.number_input('concave points worst')	

        symmetry_worst = st.number_input('symmetry worst')	

        fractal_dimension_worst = st.number_input('fractal dimension worst')


    # code untuk prediksi
    kanker_diagnosis = ''

    # membuat tombol untuk prediksi
    if st.button('Test Prediksi Kanker'):
        kanker_prediction = kanker_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])
        st.write(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst)
        if(kanker_prediction == 1):
            kanker_diagnosis = 'Kanker Jinak'
        else:
            kanker_diagnosis = 'Kanker Ganas'
        
        st.success(kanker_diagnosis)
        


