# streamlit app

import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('calories_clean.csv')

st.set_page_config(layout="wide")
st.title('Calorie Lookup')

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.header('Calorie Range')
        min_calories = st.slider('Min. Calorie', 0, 1009, 0)
        max_calories = st.slider('Max. Calorie', 0, 1009, 1009)
    
        filter_data = df[(df['Cals_per100grams'] >= min_calories) & (df['Cals_per100grams'] <= max_calories)]
        st.write(filter_data)
        
        plt = px.bar(filter_data, x='Cals_per100grams', y='FoodItem', orientation='h')
        st.plotly_chart(plt)
        
    with col2:
        food_item = st.selectbox('Food Item', df['FoodItem'].unique())
        if food_item:
            food_data = df[df['FoodItem'] == food_item]
            st.write(food_data)
        else:
            st.write('No data found')
            
            
# Footer with my info

with st.container():
    st.markdown("---")
    st.write("Created by [Saadat Khalid](https://www.linkedin.com/in/saadatawan/) with :heart:")
    st.write("25-June-2024")

    st.markdown("---")
    
