import streamlit as st
import pandas as pd
from utils import save_dataframe


st.set_page_config(page_title="Edit Product", page_icon="✏️")
st.title("Edit Product")

if not st.session_state["products_df"].empty:
    product_names = st.session_state["products_df"]["Product Name"].tolist()
    search_product = st.selectbox("Product Name", options=[""] + product_names)
    if search_product:
        product_row = st.session_state["products_df"][
            st.session_state["products_df"]["Product Name"] == search_product
        ].index[0]
        new_name = st.text_input("Product Name", value=search_product)
        new_price = st.number_input(
            "Price",
            min_value=0,
            step=1,
            value=int(st.session_state["products_df"].loc[product_row, "Price"]),
        )
        if st.button("Save Changes"):
            st.session_state["products_df"].at[product_row, "Product Name"] = new_name
            st.session_state["products_df"].at[product_row, "Price"] = new_price
            save_dataframe()
            st.success(f'Product "{new_name}" has been updated.')
else:
    st.error("No products available.")
