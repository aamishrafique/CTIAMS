import streamlit as st
import pandas as pd
from utils import save_dataframe


st.set_page_config(page_title="Add Product")
st.title("Add Product")

name = st.text_input("Product Name", key="name")
price = st.number_input("Price", min_value=0, step=1, key="price")

if st.button("Add Product"):
    if name.strip() and price > 0:
        new_product = pd.DataFrame([[name, price]], columns=["Product Name", "Price"])
        st.session_state["products_df"] = pd.concat(
            [st.session_state["products_df"], new_product], ignore_index=True
        )
        st.success(f'Product "{name}" with price Rs. {price} has been added.')
        save_dataframe()
    elif price <= 0:
        st.error("Price must be greater than 0.")
    else:
        st.error("Product name cannot be empty.")
