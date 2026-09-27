import streamlit as st
from src.database.db import create_subject


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


def share_subject_dialoge(name, subject_code):
    