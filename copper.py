import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu
import pandas as pd

df = pd.read_csv('Copper.csv')

compressed_pickle_file = 'Selling_price_reg.pkl'

with open(compressed_pickle_file, 'rb') as f:
    reg_model = pickle.load(f)

pickle_file = 'Status_class.pkl'

with open(pickle_file, 'rb') as f:
    class_model = pickle.load(f)

# Functions
def status_prediction(country, item_type, application, width, product_ref, quantity_tons_log,
                      customer_log, thickness_log, selling_price_log, item_date_day,
                      item_date_month, item_date_year, delivery_date_day, delivery_date_month,
                      delivery_date_year):

    item_date_day = int(item_date_day)
    item_date_month = int(item_date_month)
    item_date_year = int(item_date_year)

    delivery_date_day = int(delivery_date_day)
    delivery_date_month = int(delivery_date_month)
    delivery_date_year = int(delivery_date_year)

    user_data = np.array([[country, item_type, application, width, product_ref, quantity_tons_log,
                           customer_log, thickness_log, selling_price_log, item_date_day,
                           item_date_month, item_date_year, delivery_date_day, delivery_date_month,
                           delivery_date_year]])
    
    y_pred = class_model.predict(user_data)

    return 1 if y_pred == 1 else 0

def SP_prediction(country, status, item_type, application, width, product_ref, quantity_tons_log,
                  customer_log, thickness_log, item_date_day, item_date_month, item_date_year,
                  delivery_date_day, delivery_date_month, delivery_date_year):

    item_date_day = int(item_date_day)
    item_date_month = int(item_date_month)
    item_date_year = int(item_date_year)

    delivery_date_day = int(delivery_date_day)
    delivery_date_month = int(delivery_date_month)
    delivery_date_year = int(delivery_date_year)

    user_data = np.array([[country, status, item_type, application, width, product_ref, quantity_tons_log,
                           customer_log, thickness_log, item_date_day, item_date_month, item_date_year,
                           delivery_date_day, delivery_date_month, delivery_date_year]])
    
    y_pred = reg_model.predict(user_data)

    y_pred_proba = np.exp(y_pred[0])

    return y_pred_proba

st.set_page_config(layout="wide")

st.title(":red[**INDUSTRIAL COPPER MODELING**]")

with st.sidebar:
    option = option_menu('MAIN MENU', options=["SELLING PRICE PREDICTION", "STATUS PREDICTION"])

if option == "STATUS PREDICTION":

    st.subheader("**STATUS PREDICTION (:green[WIN] OR :red[LOSE])**")
    st.write(" ")

    col1, col2 = st.columns(2)

    with col1:
        country = st.number_input(label="**COUNTRY**", min_value=25.0, max_value=113.0, step=0.0)
        item_type = st.number_input(label="**ITEM TYPE**", min_value=0.0, max_value=6.0, step=0.0)
        application = st.number_input(label="**APPLICATION**", min_value=2.0, max_value=87.5, step=0.0)
        width = st.number_input(label="**WIDTH**", min_value=700.0, max_value=1980.0, step=0.0)
        product_ref = st.number_input(label="**PRODUCT_REF** ", min_value=611728.0, max_value=1722207579.0, step=0.0)
        quantity_tons_log = st.number_input(label="**QUANTITY_TONS (Log Value)**", format="%0.15f", min_value=-0.3223343801166147, max_value=6.924734324081348, step=0.0)
        customer_log = st.selectbox("**CUSTOMER (Log Value)**", df['customer_log'].unique())
        thickness_log = st.number_input(label="**THICKNESS (Log Value)**", format="%0.15f", min_value=-1.7147984280919266, max_value=3.281543137578373, step=0.0)

    with col2:
        selling_price_log = st.number_input(label="**SELLING PRICE (Log Value)**/ Min:5.97503, Max:7.39036", format="%0.15f", min_value=5.97503, max_value=7.39036, step=0.0)
        item_date_day = st.selectbox("**ITEM DATE**", df['item_date_day'].unique())
        item_date_month = st.selectbox("**ITEM MONTH**", df['item_date_month'].unique())
        item_date_year = st.selectbox("**ITEM YEAR**", df['item_date_year'].unique())
        delivery_date_day = st.selectbox("**DELIVERY DATE**", df['delivery_date_day'].unique())
        delivery_date_month = st.selectbox("**DELIVERY MONTH**", df['delivery_date_month'].unique())
        delivery_date_year = st.selectbox("**DELIVERY YEAR**", df['delivery_date_year'].unique())

    button = st.button(":red[**PREDICT THE STATUS**]", use_container_width=True)

    if button:
        status = status_prediction(country, item_type, application, width, product_ref, quantity_tons_log,
                                   customer_log, thickness_log, selling_price_log, item_date_day,
                                   item_date_month, item_date_year, delivery_date_day, delivery_date_month,
                                   delivery_date_year)
        
        if status == 1:
            st.success("**STATUS : WON**")
        else:
            st.warning("**STATUS : LOSE**")

if option == "SELLING PRICE PREDICTION":

    st.subheader("**SELLING PRICE PREDICTION**")
    st.write(" ")

    col1, col2 = st.columns(2)

    with col1:
        country = st.number_input(label="**COUNTRY**", min_value=25.0, max_value=113.0, step=0.0)
        status = st.number_input(label="**STATUS**", min_value=0.0, max_value=8.0, step=0.0)
        item_type = st.number_input(label="**ITEM TYPE**", min_value=0.0, max_value=6.0, step=0.0)
        application = st.number_input(label="**APPLICATION**", min_value=2.0, max_value=87.5, step=0.0)
        width = st.number_input(label="**WIDTH**", min_value=700.0, max_value=1980.0, step=0.0)
        product_ref = st.number_input(label="**PRODUCT_REF** ", min_value=611728.0, max_value=1722207579.0, step=0.0)
        quantity_tons_log = st.number_input(label="**QUANTITY_TONS (Log Value)**", format="%0.15f", min_value=-0.3223343801166147, max_value=6.924734324081348, step=0.0)
        customer_log = st.selectbox("**CUSTOMER (Log Value)**", df['customer_log'].unique())

    with col2:
        thickness_log = st.number_input(label="**THICKNESS (Log Value)**", format="%0.15f", min_value=-1.7147984280919266, max_value=3.281543137578373, step=0.0)
        item_date_day = st.selectbox("**ITEM DATE**", df['item_date_day'].unique())
        item_date_month = st.selectbox("**ITEM MONTH**", df['item_date_month'].unique())
        item_date_year = st.selectbox("**ITEM YEAR**", df['item_date_year'].unique())
        delivery_date_day = st.selectbox("**DELIVERY DATE**", df['delivery_date_day'].unique())
        delivery_date_month = st.selectbox("**DELIVERY MONTH**", df['delivery_date_month'].unique())
        delivery_date_year = st.selectbox("**DELIVERY YEAR**", df['delivery_date_year'].unique())

    button = st.button(":red[**PREDICT THE SELLING PRICE**]", use_container_width=True)

    if button:
        price = SP_prediction(country, status, item_type, application, width, product_ref, quantity_tons_log,
                              customer_log, thickness_log, item_date_day, item_date_month, item_date_year,
                              delivery_date_day, delivery_date_month, delivery_date_year)
        
        st.success(f"**The Selling Price is :** {price}")
