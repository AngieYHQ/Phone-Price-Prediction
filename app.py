import streamlit as st
import pandas as pd
import pickle
import numpy as np
from pycaret.regression import load_model 
from sklearn.preprocessing import LabelEncoder


#Load data
df = pd.read_csv('data_to_map.csv')

# set app configuration
st.set_page_config(page_title='Phone Price App', page_icon='📱', layout='wide', initial_sidebar_state='expanded')
    
#set app title
st.title('📱Phone Price App')
    
# create input widgets
st.sidebar.subheader('Select phone features')
# create sidebar widgets
#create a streamlit variable that stores the features and options
os_st = st.sidebar.selectbox('Operating System',['IOS','Android'])
brand_st = st.sidebar.selectbox('Brand',['apple','samsung','oppo','huawei'])
phone_st = st.sidebar.selectbox('Phone Model', ['iPhone 11', 'iPhone 14', 'iPhone 11 pro', 'iPhone 13 Pro',
       'iPhone X', 'iPhone 11 Pro Max', 'iPhone 14 Pro Max', 'iPhone  XR',
       'iPhone 13 Pro Max', 'iPhone XS', 'iPhone 7 Plus', 'iPhone 4',
       'iPhone 12', 'iPhone XS Max', 'iPhone 12 Mini', 'iPhone 12 Pro',
       'iPhone 12 Pro Max', 'iPhone 13', 'iPhone 7', 'Galaxy Z Flip 4',
       'Galaxy S 9', 'Galaxy A A32', 'Galaxy S 8', 'Galaxy S 23 Ultra',
       'Galaxy A A 23', 'Galaxy Note 20', 'Galaxy S 21 Plus',
       'Galaxy Z Fold 4', 'Galaxy S 22 Ultra', 'Galaxy S 21 Ultra',
       'Galaxy Z Flip 3', 'Galaxy S 21', 'Galaxy S 20 FE',
       'Galaxy S 9 Plus', 'Galaxy A A23', 'Galaxy Note 10', 'Galaxy S 22',
       'Galaxy S 10 Plus', 'Reno 7 Z', 'Reno 4 Pro', 'Find X3 Pro',
       'Oppo A 16', 'Reno 5 Pro', 'Reno 6 Pro', 'Reno 8', 'Reno 10',
       'Oppo A 57', 'Oppo A 96', 'Find N2 flip', 'Reno 2', 'Reno 3',
       'Reno 3 Pro', 'Find X5 Pro', 'Reno 7', 'Reno 4 pro', 'Reno 9',
       'Oppo A 31', 'Reno 8 Pro', 'Find X2 Pro', 'Oppo A 95', 'R11S R11S',
       'Oppo A 17K', 'Oppo A 53', 'Find Pro 5G', 'Mate 10', 'Mate 30',
       'P 20 Pro', 'P 30 Lite', 'Mate 20X', 'Nova 5 T', 'Mate 20',
       'P 40 Pro', 'P 30 Pro', 'Mate 20 Pro', 'Mate 30 Pro',
       'Mate 10 Pro', 'Nova 3i', 'P 50 Pro', 'Mate 40 Pro', 'Nova 7 SE',
       'P 40', 'Mate 50 Pro', 'iPhone 14 Pro', 'iPhone 8 Plus',
       'iPhone 8', 'Galaxy Z Fold 3', 'Galaxy Note 10 Plus',
       'Galaxy S 20', 'Galaxy A A73', 'Galaxy Note 20 ultra', 'Fold 4',
       'Galaxy Note 9', 'Reno 7 Pro', 'Reno 10x Zoom', 'Oppo A 76',
       'Reno 5Z', 'Find N2 Flip', 'Oppo A X5S', 'Reno 10X Zoom',
       'Reno 8 pro', 'Reno 8T', 'Find X2 Pro ', 'Mate Pad 10.4 ',
       'Honor 8c MAX', 'Nova 2i', 'P 20', 'Y 6 Pro', 'Honor 8c',
       'Mate Pad Pro ', 'Nova 7i', 'P 40 pro plus', 'P 10'])
capacity_st = st.sidebar.selectbox('Storage Capacity', ['6', '8','32','64','128','256','512'])
condition_st = st.sidebar.selectbox('Physical Condition',['Heavily used', 'Brand new', 'Lightly used', 'Well used', 'Like new'])
battery_st = st.sidebar.selectbox('Battery Health',[68, 72, 73, 75, 77, 79, 80, 83, 85, 86, 87, 90, 91, 92, 98, 100])
warranty_st = st.sidebar.selectbox('Manufacturing Warranty',['yes', 'no'])
reviews_st = st.sidebar.selectbox('Number of Seller Reviews',['0-100','101-1000','1001-2000','2001-5000'])

# Generate prediction based on user selected attributes
# Create a dataframe to store streamlit variables created above, newdfcolumns: streamlit variables
st.subheader('Variables in Data Set')
input_df = pd.DataFrame({'os': [os_st], 'brand': [brand_st], 'phone': [phone_st], 'capacity': [capacity_st], 'condition': [condition_st], 'battery': [battery_st], 'warranty': [warranty_st], 'reviews': [reviews_st]})
st.write(input_df)
# replace string values with encoded values
input_df['os'] = input_df['os'].map({'IOS': 0, 'Android': 1})
input_df['brand'] = input_df['brand'].map({'apple':0, 'samsung':1, 'oppo':2, 'huawei': 3}) 


# instantiate the encoder
encoder = LabelEncoder()

# fit the encoder to the 'phone' column
encoder.fit(input_df['phone'])

# transform the 'phone' column using the fitted encoder
input_df['phone'] = encoder.transform(input_df['phone'])


input_df['condition'] = input_df['condition'].map({'Brand new':0, 'Like new':1, 'Lightly used':2, 'Well used': 3, "Heavily used":4}) 
input_df['warranty'] = input_df['warranty'].map({'no':0, 'yes':1}) 
input_df['reviews'] = input_df['reviews'].map({'0-100':90,'101-1000':1000,'1001-2000':2000,'2001-5000':3000})


#dropnain capacity, convert type to int
input_df = input_df[pd.to_numeric(input_df['capacity'], errors='coerce').notnull()]
input_df['capacity'] = input_df['capacity'].astype(int)



# load the saved model
model = load_model('rfmodel')

# make prediction
prediction = model.predict(input_df)

# display the prediction
st.subheader('Prediction')
st.write('The recommended sale price is $', np.round(prediction[0], 2))
