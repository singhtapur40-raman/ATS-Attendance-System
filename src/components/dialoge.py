import streamlit as st
from src.database.db import create_subject, enroll_student_to_subject, create_attendance
import segno 
import io
from PIL import Image
from src.database.config import supabase
import time
from src.pipelines.voice_pipeline import process_bulk_audio
from datetime import datetime
import pandas as pd

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
        st.image(out.getvalue(), use_container_width=True, caption='QR-Code for joining class')


@st.dialog("Enroll in Subject")
def enroll_dialogue():
    st.write('Enter the subject code:')
    join_code = st.text_input('Subject Code', placeholder='Eg: CS102M')

    if st.button('Enroll Now!!', type='primary', width='stretch'):
        if join_code: 
            res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', join_code).execute()
            if res.data:
                subject = res.data[0]
                stud_id = st.session_state.student_data['student_id']

                check = supabase.table('subject_students').select('*').eq('subject_id', subject["subject_id"]).eq('student_id', stud_id).execute()
                if check.data:
                    st.warning('You are already enrolled in this program!')
                else:
                    enroll_student_to_subject(stud_id, subject['subject_id'])
                    st.success('Successfully Enrolled!')
                    time.sleep(1)
                    st.rerun()
        else: 
            st.warning('Please enter a valid subject code!')


@st.dialog("Auto Enrollment")
def auto_enroll_dialog(code):
    student_id = st.session_state.student_data['student_id']

    resp = supabase.table('subjects').select('subject_id, name').eq('subject_code', code).execute()
    if not resp.data:
        st.error('Subject Code not found!')
        if st.button('Close'):
            st.query_params.clear()
            st.rerun()
        return
    
    subject = resp.data[0]

    check = supabase.table('subject_students').select('*').eq('subject_id', subject["subject_id"]).eq('student_id', student_id).execute()
    if check.data:
        st.info("You're already enrolled!")
        if st.button('Got it!'):
            st.query_params.clear()
            st.rerun()
        return
    
    st.markdown(f'Would you like to enroll in **{subject['name']}**?')

    col1, col2 = st.columns(2)

    with col1:
        if st.button('No thanks'):
            st.query_params.clear()
            st.rerun()
    
    with col2:
        if st.button('Yes enroll now!', type='primary', width='stretch'):
            enroll_student_to_subject(student_id, subject['subject_id'])
            st.success('Joined Successfully!')
            st.query_params.clear()
            time.sleep(2)
            st.rerun()


@st.dialog("Capture or Add photos")
def add_photos_dialog():

    st.write('Add Classroom photos to scan for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = 'primary' if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'

    
    with t2:
        type_upload = 'primary' if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')
        if cam_photo :
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast('Photo Captured!')
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader('Choose image files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='dialog_upload')

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.toast('Photos Uploaded Successfully..')
            st.rerun()

    st.divider()

    if st.button('Done!', type='primary', width='stretch'):
        st.rerun()


def show_attendance_result(df, logs):
        st.write("Please review attendance before confirming..")
        st.dataframe(df, hide_index=True, width='stretch')

        col1, col2 = st.columns(2)

        with col1:
            if st.button('Discard', width='stretch'):
                st.session_state.voice_attendance_results = None
                st.session_state.attendance_images = []
                st.rerun()

        with col2:
            if st.button('Confirm & Save', width='stretch', type='primary'):
                try:
                    create_attendance(logs)
                    st.toast("Attendance Taken!!")
                    st.session_state.attendance_images = []
                    st.session_state.voice_attendance_results = None
                    st.rerun()

                except Exception as e:
                    st.error('Sync Failed!')


@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)




@st.dialog("Voice Attendance")
def voice_attendance_dialog(subj_id):
    st.write("Record student's voice saying I am present.")

    audio_data = None

    audio_data = st.audio_input("Record Classroom audio")

    if st.button('Analyze Audio', width='stretch', type='primary'):
        with st.spinner('Processing Audio data'):
            enrolled_resp = supabase.table('subject_students').select('*, students(*)').eq('subject_id', subj_id).execute()
            enrolled_students = enrolled_resp.data

            if not enrolled_students:
                st.warning('No students enrolled in this course.')
                return
            
            candidates_dict = {
                s['students']['student_id'] : s['students']['voice_embedding']
                for s in enrolled_students if s['students'].get('voice_embedding')
            }

            if not candidates_dict:
                st.error("No enrolled students have voice profile registered..")
                return
            
            audio_bytes = audio_data.read()

            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendance_to_log = [], []

            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node['students']
                score = detected_scores.get(student['student_id'], 0.0)
                is_present = bool(score > 0)

                results.append({
                    "Name" : student['name'], 
                    "ID" : student['student_id'],
                    "Source" : score if is_present else "-", 
                    "Status" : "✅ Present" if is_present else "❌ Absent"
                })

                attendance_to_log.append({
                    'student_id' : student['student_id'], 
                    'subject_id' : subj_id, 
                    'timestamp' : current_timestamp, 
                    'is_present' : bool(is_present)
                })

            st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)

    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_result(df_results, logs)


        



                 
