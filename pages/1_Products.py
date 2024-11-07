import streamlit as st
from utils import save_dataframe


st.set_page_config(page_title="Products")
st.title("Products")
if not st.session_state["products_df"].empty:
    st.session_state["products_df"].index.name = "Index"
    st.dataframe(st.session_state["products_df"], use_container_width=True)
else:
    st.error("No products available.")

save_dataframe()
