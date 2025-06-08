import streamlit as st

home_page = st.Page("pages/web.py", title="Home", icon="🔥")
about_page = st.Page("pages/about.py", title="About", icon=":material/favorite:")

pg = st.navigation([home_page, about_page])
st.set_option("client.toolbarMode","viewer")
st.set_page_config(page_title="Sir. Andrew Gotham's Scholar ToDo App", page_icon="🔥")
pg.run()