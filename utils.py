import pandas as pd
import streamlit as st


PRODUCTS_FILE_PATH = "products.csv"


def initialize_dataframe():
    if "products_df" not in st.session_state:
        try:
            st.session_state["products_df"] = pd.read_csv(PRODUCTS_FILE_PATH)
        except FileNotFoundError:
            st.session_state["products_df"] = pd.DataFrame(
                columns=["Product Name", "Price"]
            )


def save_dataframe():
    st.session_state["products_df"].to_csv(PRODUCTS_FILE_PATH, index=False)
