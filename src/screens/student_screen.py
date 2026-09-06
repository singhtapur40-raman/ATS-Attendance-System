import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout
 
def student_screen():

    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')

    with c1:
        header_dashboard()

    with c2:
        if st.button('GO BACK TO HOME!', type='secondary', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_type']=None
            st.rerun()
    
    st.space()
    st.space()

    st.header("Login using FaceID", text_alignment='center')
    st.camera_input("Position your face in the center!")
    footer_dashboard()