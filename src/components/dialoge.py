import streamlit as st
from src.database.db import create_subject
import segno 
import io


@st.dialog("Create New Subject")
def create_subject_dialoge(teacher_id):

    st.write("Enter the details of New Subject")

    subj_id = st.text_input("Subject Code", placeholder='CS101')
    subj_name = st.text_input("Subject Name", placeholder='Engineering Mathematics')
    subj_section = st.text_input("Section", placeholder='CSE20')

    if st.button("Create Subject Now", type='primary', width='stretch'):
        if subj_id and subj_name and subj_section:
            try:
                create_subject(subj_id, subj_name, subj_section, teacher_id)
                st.toast("Subject Created Successfully")
                st.rerun()
            except Exception as e:
                st.error(f"Error : {str(e)}")
        else:
            st.warning("Please fill all the fields!")


@st.dialog("Share Class Link")
def share_subject_dialoge(name, subject_code):
    app_domain = "https://localhost:8501"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join!")

    qr = segno.make(join_url)

    out = io.BytesIO()

    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Copy Link') 
        st.code(join_url, language='text')
        st.code(subject_code, language='text')
        st.info('Copy this link to share on Whatsapp or E-mail')


    with col2: 
        st.markdown('### scan to Join')
        st.image(out.getvalue(), use_column_width=True, caption='QR-Code for joining class')